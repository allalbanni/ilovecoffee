# Project Summary - Automated PDF Marking System

## 📁 Project Structure

```
ilovecoffee/
├── app.py                      # Main Streamlit application interface
├── pdf_processor.py            # PDF handling & OCR extraction module
├── marking_engine.py           # Answer comparison & marking logic
├── requirements.txt            # Python dependencies
├── config.ini                  # Configuration settings (optional)
├── README.md                   # Complete documentation
├── QUICKSTART.md               # Quick setup guide
├── run.bat                     # Windows startup script
├── run.sh                      # macOS/Linux startup script
├── sample_markscheme.json      # Example markscheme (JSON format)
└── sample_markscheme.txt       # Example markscheme (TXT format)
```

## 📚 File Descriptions

### Core Application Files

**app.py** (Main Application)
- Streamlit web interface
- 3-tab interface: Upload, Configure, Results
- File upload handling
- Real-time processing status
- Results display and PDF download

**pdf_processor.py** (PDF Module)
- Extract text from PDF using OCR (Tesseract)
- Annotate PDFs with marking results
- Generate formatted feedback reports
- Handle PDF to image conversion

**marking_engine.py** (Marking Logic)
- Parse markscheme in multiple formats
- Extract answers from OCR text
- Compare student vs expected answers
- 3 marking modes: Strict, Flexible, Keyword
- Calculate similarity scores
- Generate detailed feedback

### Configuration & Documentation

**requirements.txt**
- Streamlit 1.31.1 (web framework)
- pytesseract 0.3.10 (OCR interface)
- pdf2image 1.16.3 (PDF conversion)
- PyPDF2 4.0.1 (PDF manipulation)
- reportlab 4.0.7 (PDF generation)
- Pillow 10.1.0 (image processing)

**config.ini**
- OCR settings (language, DPI, path)
- Marking defaults (threshold, mode)
- PDF output settings
- UI preferences
- Logging configuration

**README.md**
- Full documentation
- Installation instructions
- Usage guide
- Markscheme format examples
- Troubleshooting section

**QUICKSTART.md**
- 5-minute setup guide
- System dependencies
- First run example
- Quick troubleshooting

### Startup Scripts

**run.bat** (Windows)
- Automatic virtual environment setup
- Dependency installation check
- Application launch
- One-click startup

**run.sh** (macOS/Linux)
- Bash version of startup script
- Same functionality as batch file

### Sample Files

**sample_markscheme.json**
- 5 sample questions with answers
- JSON format for structured data
- Easy to use as template

**sample_markscheme.txt**
- Same 5 questions in text format
- Human-readable Q&A format
- Shows alternative format

## 🔄 Application Flow

```
User Opens Browser
        ↓
[UPLOAD TAB] - Choose student PDF + markscheme
        ↓
[CONFIGURE TAB] - Set marking parameters
        ↓
[RESULTS TAB] - Click "Process and Mark"
        ↓
app.py processes uploads
        ↓
pdf_processor.py extracts OCR text
        ↓
marking_engine.py compares answers
        ↓
Generate two output PDFs:
    ├─ Annotated PDF (corrections on original)
    └─ Feedback Report (detailed results)
        ↓
Display results & download options
```

## 🎯 Key Features

### 1. OCR Text Extraction
- Converts PDF pages to images
- Uses Tesseract OCR engine
- Preserves page structure information
- Handles multiple pages

### 2. Answer Parsing
- Extracts Q&A pairs from OCR text
- Supports various question numbering styles
- Handles multi-line answers
- Recognizes common patterns (Q1:, 1., Question 1:, etc.)

### 3. Intelligent Marking
- **Strict Mode:** Exact match only
- **Flexible Mode:** Similarity-based (configurable threshold)
- **Keyword Mode:** Key term matching (70% required)

### 4. Markscheme Flexibility
- JSON format (structured data)
- Text format (human-readable Q&A)
- PDF format (scanned marksheets)
- Automatic format detection

### 5. Comprehensive Output
- Annotated PDF with marking indicators
- Detailed feedback report PDF
- Score statistics and percentage
- Question-by-question breakdown
- Similarity scores for each answer

### 6. User Interface
- Clean, intuitive Streamlit interface
- Real-time processing feedback
- Live result preview
- Easy file download

## 🔧 Technology Stack

- **Frontend:** Streamlit (Python web framework)
- **Backend:** Python 3.8+
- **OCR:** Tesseract (via pytesseract)
- **PDF Processing:** PyPDF2, reportlab
- **Image Processing:** Pillow, pdf2image
- **Text Matching:** difflib, regex

## 📊 Supported Formats

**Input - Student Answers:**
- PDF files (scanned or digital)

**Input - Markscheme:**
- PDF files (scanned marksheets)
- TXT files (text format)
- JSON files (structured data)

**Output:**
- PDF (annotated original)
- PDF (detailed feedback report)

## ⚙️ System Requirements

- Python 3.8+
- Tesseract OCR (system dependency)
- Poppler (system dependency)
- 2GB+ RAM (recommended for large PDFs)
- Internet connection (not required after initial setup)

## 📈 Scalability

Current implementation handles:
- Single PDF processing
- Up to 50MB file uploads
- Documents with 50+ pages
- Markschemes with 100+ questions

Future enhancements could add:
- Batch processing of multiple PDFs
- Database storage
- User sessions
- Performance optimization

## 🚀 Deployment Options

### Local Development
```bash
streamlit run app.py
```

### Docker Deployment
Create Dockerfile with system dependencies and Python packages

### Cloud Deployment
- Streamlit Cloud
- Heroku
- AWS Lambda
- Google Cloud Run

## 📝 Usage Example

1. **Prepare Files:**
   - student_answers.pdf (scanned answer sheet)
   - markscheme.json (expected answers)

2. **Run Application:**
   - `run.bat` (Windows) or `./run.sh` (Mac/Linux)
   - Opens http://localhost:8501

3. **Upload & Process:**
   - Upload both files
   - Configure settings
   - Click "Process and Mark"

4. **Get Results:**
   - View feedback in browser
   - Download 2 PDFs
   - Grading complete!

## 🔐 Privacy & Security

- Files processed locally (not uploaded to servers)
- No data storage between sessions
- Temporary files cleaned up after processing
- No external APIs required (except local Tesseract)

## 📞 Support & Customization

The codebase is well-commented and modular:
- Easy to modify marking logic
- Customizable output formats
- Extensible for new features
- Can integrate with learning management systems

---

**Version:** 1.0  
**Created:** May 2026  
**Language:** Python 3.8+  
**License:** Open Source
