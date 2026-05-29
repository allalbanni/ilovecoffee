# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Step 1: Install System Dependencies (One-time setup)

**Windows:**
1. Install Tesseract OCR:
   - Download: https://github.com/UB-Mannheim/tesseract/wiki
   - Run the installer (choose default path: `C:\Program Files\Tesseract-OCR`)
   
2. Install Poppler:
   - Download: https://github.com/oschwartz10612/poppler-windows/releases/
   - Extract and add to PATH, or install via Chocolatey: `choco install poppler`

**macOS:**
```bash
brew install tesseract
brew install poppler
```

**Linux:**
```bash
sudo apt-get install tesseract-ocr
sudo apt-get install poppler-utils
```

### Step 2: Install Python Dependencies

**Windows:**
```bash
# Double-click run.bat
# OR manually:
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**macOS/Linux:**
```bash
# Make script executable
chmod +x run.sh

# Run it
./run.sh
```

### Step 3: Launch the Application

**Windows:** Double-click `run.bat`

**macOS/Linux:** Run `./run.sh`

The application opens at: **http://localhost:8501**

---

## 📋 First Run Example

### Using the Sample Markscheme

1. **Create a test PDF** (or use your own):
   - Create a simple text document with:
     ```
     Q1: Paris
     Q2: Star
     Q3: Light energy conversion process
     Q4: Powerhouse of the cell
     Q5: 300000 km/s
     ```
   - Save as PDF (use "Print to PDF" in Word)

2. **Upload Files:**
   - Student PDF: Your test PDF
   - Markscheme: Use `sample_markscheme.json`

3. **Configure:**
   - Threshold: 80%
   - Ignore Case: ✓ (checked)
   - Mode: Flexible

4. **Process:**
   - Click "Process and Mark"
   - Wait for processing (usually 10-30 seconds)
   - Review feedback
   - Download results

---

## 🔧 Troubleshooting

### "Tesseract not found"
- Make sure Tesseract is installed
- Restart your terminal/IDE
- Check installation path

### "pdf2image fails"
- Install poppler-utils
- Restart the application

### "No module named 'streamlit'"
- Activate virtual environment
- Run: `pip install -r requirements.txt`

### "OCR produces gibberish"
- Check if PDF is clear and readable
- Try scanning at higher resolution
- Use a simpler test PDF first

---

## 📊 Understanding Results

### Score Breakdown
- **Total Questions:** Number of questions marked
- **Correct Answers:** Matching the markscheme
- **Score:** Percentage correct
- **Incorrect:** Number wrong

### Similarity Score
- **100%:** Perfect match
- **80%+:** Very similar (accepted in Flexible mode)
- **60-80%:** Partially correct
- **<60%:** Significantly different

---

## 💡 Tips for Best Results

1. **Use clear PDFs:** Blurry or handwritten text = poor OCR
2. **Structured markscheme:** Clear Q&A format works best
3. **Start simple:** Test with 5 questions before larger exams
4. **Adjust threshold:** Lower threshold = more lenient marking

---

## 📞 Need Help?

- Check README.md for detailed documentation
- Review sample_markscheme.json for format examples
- Test with sample files first

---

**Enjoy automated marking!** ✨
