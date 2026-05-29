# Automated PDF Marking System

An intelligent web application that automatically marks student answer PDFs using a markscheme, extracts answers through OCR, and generates corrected feedback documents.

## Features

✨ **Core Features:**
- 📄 PDF text extraction using OCR (Tesseract)
- 🔍 Intelligent answer comparison and matching
- 📝 Multiple marking modes (Strict, Flexible, Keyword-based)
- 📊 Automatic scoring and grading
- 📥 Dual output: Annotated PDF + Feedback Report
- 🎨 User-friendly web interface

## Requirements

### System Requirements
- Python 3.8+
- Tesseract OCR (required for PDF text extraction)
- poppler-utils (required for PDF to image conversion)

### Python Dependencies
- streamlit (web framework)
- pytesseract (OCR interface)
- pdf2image (PDF conversion)
- PyPDF2 (PDF manipulation)
- reportlab (PDF generation)
- Pillow (image processing)

## Installation

### 1. Install System Dependencies

**Windows:**
```bash
# Install Tesseract OCR
# Download from: https://github.com/UB-Mannheim/tesseract/wiki
# Or use chocolatey: choco install tesseract

# Install poppler
# Download from: https://github.com/oschwartz10612/poppler-windows/releases/
# Or use chocolatey: choco install poppler
```

**macOS:**
```bash
brew install tesseract
brew install poppler
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install tesseract-ocr
sudo apt-get install poppler-utils
```

### 2. Install Python Dependencies

```bash
# Navigate to project directory
cd c:\Users\AHMED\ilovecoffee

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure Tesseract Path (Windows Only)

If Tesseract is not in your system PATH, add this to the top of `app.py`:

```python
import pytesseract
pytesseract.pytesseract.pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

## Usage

### Running the Application

```bash
# Make sure virtual environment is activated
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

### Workflow

1. **Upload Files Tab:**
   - Upload the student's answer PDF
   - Upload the markscheme (PDF, TXT, or JSON format)

2. **Configure Tab:**
   - Set matching threshold (0-100%)
   - Choose case sensitivity
   - Select marking mode

3. **Results Tab:**
   - Click "Process and Mark" button
   - Wait for OCR and comparison to complete
   - View detailed feedback
   - Download corrected PDFs

## Markscheme Format

The application supports multiple markscheme formats:

### Text Format
```
Q1: Expected answer for question 1
Q2: Expected answer for question 2
Q3: Expected answer for question 3
```

### Numbered Format
```
1. First answer
2. Second answer
3. Third answer
```

### JSON Format
```json
{
  "1": "First answer",
  "2": "Second answer",
  "3": "Third answer"
}
```

## Marking Modes

### 1. Strict Mode
- Requires exact match (with optional case insensitivity)
- Best for: Questions with specific, unambiguous answers

### 2. Flexible Mode
- Uses similarity scoring (default threshold: 80%)
- Tolerates minor spelling/formatting differences
- Best for: Longer answers, essays, definitions

### 3. Keyword Mode
- Checks for presence of key terms
- At least 70% of key terms must match
- Best for: Conceptual answers, definitions

## Output Files

The system generates two PDF files:

1. **marked_answers_annotated.pdf**
   - Original student PDF with marking annotations
   - Shows correct/incorrect status for each answer

2. **feedback_report.pdf**
   - Comprehensive feedback report
   - Summary statistics
   - Detailed feedback for each question
   - Similarity scores

## File Structure

```
ilovecoffee/
├── app.py                 # Main Streamlit application
├── pdf_processor.py       # PDF handling module
├── marking_engine.py      # Answer comparison and marking
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Example Usage

### Step 1: Prepare Files

**Student PDF:** `student_answers.pdf`
```
Q1: The capital of France is Paris
Q2: The Sun is a star
Q3: Photosynthesis is the process by which plants make food
```

**Markscheme (TXT):** `markscheme.txt`
```
Q1: Paris
Q2: Star
Q3: Process where plants convert light into chemical energy
```

### Step 2: Upload and Process

1. Open the application
2. Upload `student_answers.pdf` and `markscheme.txt`
3. Adjust settings if needed
4. Click "Process and Mark"

### Step 3: Review Results

- See score breakdown
- Review individual feedback
- Download the generated PDFs

## Troubleshooting

### Issue: Tesseract not found
**Solution:** Install Tesseract OCR or update the path in app.py

### Issue: PDF extraction fails
**Solution:** Ensure PDF is not encrypted. Try with a different PDF file.

### Issue: Poor OCR results
**Solution:** 
- Use high-quality PDF scans
- Ensure good image resolution
- Check that text is clearly visible

### Issue: Incorrect answers marked as correct
**Solution:**
- Lower the matching threshold
- Switch to Strict mode for exact answers
- Review the markscheme format

### Issue: ModuleNotFoundError
**Solution:** Ensure virtual environment is activated and all requirements are installed

## Advanced Features (Future Enhancements)

- 🔐 User authentication and session management
- 💾 Database storage for marking history
- 📊 Statistical analysis and reporting
- 🤖 Machine learning-based answer understanding
- 🌐 Support for handwriting recognition
- 📱 Mobile app version
- 🔄 Batch processing multiple PDFs

## Performance Tips

- Use high-quality PDF scans for better OCR results
- Keep markscheme answers concise and clear
- For large PDFs, consider splitting into multiple files
- Adjust similarity threshold based on answer type

## Limitations

- OCR accuracy depends on PDF quality
- Handwritten answers may have lower accuracy
- Complex mathematical formulas may not be recognized
- Non-English text support depends on Tesseract configuration

## License

Open source - feel free to modify and extend as needed

## Support & Feedback

For issues or feature requests, please review the code and make improvements as needed.

## Tips for Best Results

1. **PDF Quality:** Ensure student PDFs are clear and well-formatted
2. **Markscheme:** Be specific and clear with expected answers
3. **Threshold:** Start with 80% and adjust based on results
4. **Mode Selection:** Choose the marking mode that matches your question types

---

**Version:** 1.0  
**Last Updated:** May 2026
