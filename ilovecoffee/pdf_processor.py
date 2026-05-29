"""
PDF Processing Module - Handles PDF extraction, annotation, and generation
"""

try:
    import fitz
    _MUPDF_AVAILABLE = True
except Exception:
    fitz = None
    _MUPDF_AVAILABLE = False

# Optional OCR dependencies. If unavailable, the processor will try a text-extraction fallback.
try:
    import pytesseract
    from pdf2image import convert_from_path
    _OCR_AVAILABLE = True
except Exception:
    pytesseract = None
    convert_from_path = None
    _OCR_AVAILABLE = False

from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
import io
import os


class PDFProcessor:
    """Handles PDF reading, text extraction, annotation, and report generation"""
    
    def __init__(self):
        """Initialize PDF processor"""
        self.extracted_text = None
    
    def extract_text_from_pdf(self, pdf_path):
        """
        Extract text from PDF. Prefer native text extraction; fall back to OCR when necessary.
        
        Args:
            pdf_path: Path to the PDF file
            
        Returns:
            Extracted text as string
        """
        # First attempt: try native PDF text extraction
        try:
            reader = PdfReader(pdf_path)
            extracted_text = ""
            for page in reader.pages:
                try:
                    page_text = page.extract_text() or ""
                except Exception:
                    page_text = ""
                extracted_text += f"\n" + page_text

            if extracted_text.strip():
                self.extracted_text = extracted_text.strip()
                return self.extracted_text
        except Exception:
            # If native extraction fails, we'll try OCR below (if available)
            pass

        # Fallback: try PyMuPDF text extraction first, then OCR (if dependencies are available)
        if _MUPDF_AVAILABLE and fitz is not None:
            try:
                doc = fitz.open(pdf_path)
                extracted_text = ""
                for page_num, page in enumerate(doc, 1):
                    extracted_text += "\n--- Page %s ---\n" % page_num
                    extracted_text += page.get_text()
                if extracted_text.strip():
                    self.extracted_text = extracted_text.strip()
                    return self.extracted_text
            except Exception:
                pass

        if _OCR_AVAILABLE and convert_from_path is not None and pytesseract is not None:
            try:
                images = convert_from_path(pdf_path)
                extracted_text = ""
                for page_num, image in enumerate(images, 1):
                    text = pytesseract.image_to_string(image)
                    extracted_text += f"\n--- Page {page_num} ---\n{text}"
                self.extracted_text = extracted_text
                return extracted_text
            except Exception as e:
                raise Exception(f"OCR extraction failed: {str(e)}")

        # If we reach here, no extraction method succeeded
        raise Exception(
            "Failed to extract text from PDF: native text extraction returned no text and OCR dependencies are not available. "
            "Install Tesseract and poppler, and the Python packages 'pytesseract' and 'pdf2image', or provide a text/JSON markscheme instead."
        )
    
    def annotate_pdf(self, pdf_path, marking_results):
        """
        Annotate PDF with correction marks based on marking results
        
        Args:
            pdf_path: Path to the student PDF
            marking_results: Dictionary with marking results
            
        Returns:
            BytesIO object containing the annotated PDF
        """
        try:
            reader = PdfReader(pdf_path)
            writer = PdfWriter()
            
            # For now, copy all pages as-is
            # In a production system, you would add actual annotations here
            for page in reader.pages:
                writer.add_page(page)
            
            # Write to bytes buffer
            output = io.BytesIO()
            writer.write(output)
            output.seek(0)
            
            return output
        
        except Exception as e:
            raise Exception(f"Failed to annotate PDF: {str(e)}")
    
    def generate_feedback_pdf(self, marking_results, output_path):
        """
        Generate a feedback report PDF with marking details
        
        Args:
            marking_results: Dictionary with marking results
            output_path: Path where to save the feedback PDF
        """
        try:
            # Create PDF document
            doc = SimpleDocTemplate(
                output_path,
                pagesize=letter,
                rightMargin=72,
                leftMargin=72,
                topMargin=72,
                bottomMargin=18
            )
            
            # Container for PDF elements
            elements = []
            styles = getSampleStyleSheet()
            
            # Custom styles
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=styles['Heading1'],
                fontSize=24,
                textColor=colors.HexColor('#1f77b4'),
                spaceAfter=30,
                alignment=1  # Center alignment
            )
            
            heading_style = ParagraphStyle(
                'CustomHeading',
                parent=styles['Heading2'],
                fontSize=14,
                textColor=colors.HexColor('#2ca02c'),
                spaceAfter=12,
                spaceBefore=12
            )
            
            # Title
            elements.append(Paragraph("📝 Marking Feedback Report", title_style))
            elements.append(Spacer(1, 0.3 * inch))
            
            # Summary section
            elements.append(Paragraph("Summary", heading_style))
            
            summary_data = [
                ["Metric", "Value"],
                ["Total Questions", str(marking_results.get("total_questions", 0))],
                ["Correct Answers", str(marking_results.get("correct_answers", 0))],
                ["Score", f"{marking_results.get('score_percentage', 0):.1f}%"],
                ["Incorrect", str(marking_results.get("total_questions", 0) - marking_results.get("correct_answers", 0))]
            ]
            
            summary_table = Table(summary_data, colWidths=[3*inch, 2*inch])
            summary_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1f77b4')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            
            elements.append(summary_table)
            elements.append(Spacer(1, 0.3 * inch))
            
            # Detailed feedback
            if "questions" in marking_results:
                elements.append(Paragraph("Detailed Feedback", heading_style))
                
                for i, question in enumerate(marking_results["questions"], 1):
                    status = question.get("status", "Pending").upper()
                    status_color = '#2ca02c' if status == 'CORRECT' else '#d62728'
                    
                    question_style = ParagraphStyle(
                        f'Question{i}',
                        parent=styles['Heading3'],
                        fontSize=12,
                        textColor=colors.HexColor(status_color),
                        spaceAfter=6
                    )
                    
                    elements.append(Paragraph(f"Q{i}: {status}", question_style))
                    
                    elements.append(Paragraph("<b>Student Answer:</b>", styles['Normal']))
                    elements.append(Paragraph(question.get("student_answer", "N/A"), styles['Normal']))
                    elements.append(Spacer(1, 0.1 * inch))
                    
                    elements.append(Paragraph("<b>Expected Answer:</b>", styles['Normal']))
                    elements.append(Paragraph(question.get("expected_answer", "N/A"), styles['Normal']))
                    elements.append(Spacer(1, 0.1 * inch))
                    
                    elements.append(Paragraph("<b>Feedback:</b>", styles['Normal']))
                    elements.append(Paragraph(question.get("feedback", "No feedback"), styles['Normal']))
                    
                    if "similarity" in question:
                        similarity_text = f"Similarity Score: {question['similarity']*100:.1f}%"
                        elements.append(Paragraph(similarity_text, styles['Normal']))
                    
                    elements.append(Spacer(1, 0.2 * inch))
                    elements.append(Paragraph("_" * 80, styles['Normal']))
                    elements.append(Spacer(1, 0.2 * inch))
            
            # Build PDF
            doc.build(elements)
        
        except Exception as e:
            raise Exception(f"Failed to generate feedback PDF: {str(e)}")
