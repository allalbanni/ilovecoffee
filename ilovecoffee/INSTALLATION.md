# Complete Installation Guide

## System Requirements

- **OS:** Windows, macOS, or Linux
- **Python:** 3.8 or higher
- **RAM:** 2GB minimum (4GB recommended)
- **Disk Space:** 500MB for dependencies

---

## Installation Steps

### Phase 1: Install System Dependencies

#### **WINDOWS**

**Step 1: Install Tesseract OCR**

1. Download installer from: https://github.com/UB-Mannheim/tesseract/wiki
2. Look for `tesseract-ocr-w64-setup-v5.x.x.exe`
3. Run the installer
4. Choose installation path: `C:\Program Files\Tesseract-OCR` (default)
5. Complete installation

**Verify Installation:**
```bash
tesseract --version
```

**Step 2: Install Poppler**

Option A - Manual Download:
1. Visit: https://github.com/oschwartz10612/poppler-windows/releases/
2. Download `Release-xx.zip` (latest release)
3. Extract to `C:\Program Files\poppler`
4. Add to PATH:
   - Open Environment Variables (Win+X → System → Advanced system settings)
   - Click "Environment Variables"
   - Under "System variables", find "Path" and click Edit
   - Click "New" and add: `C:\Program Files\poppler\Library\bin`
   - Click OK

Option B - Using Chocolatey:
```bash
choco install poppler
```

**Verify Installation:**
```bash
pdfinfo -v
```

---

#### **macOS**

Using Homebrew (recommended):

```bash
# Install Homebrew if you don't have it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Tesseract
brew install tesseract

# Install Poppler
brew install poppler
```

**Verify Installation:**
```bash
tesseract --version
pdfinfo -v
```

---

#### **Linux (Ubuntu/Debian)**

```bash
# Update package manager
sudo apt-get update

# Install Tesseract
sudo apt-get install -y tesseract-ocr

# Install Poppler
sudo apt-get install -y poppler-utils

# Verify installation
tesseract --version
pdfinfo -v
```

For other Linux distributions, use your package manager (yum, pacman, etc.)

---

### Phase 2: Install Python Project

#### **Step 1: Navigate to Project Directory**

```bash
cd c:\Users\AHMED\ilovecoffee
```

#### **Step 2: Create Virtual Environment**

**Windows:**
```bash
python -m venv venv
```

**macOS/Linux:**
```bash
python3 -m venv venv
```

#### **Step 3: Activate Virtual Environment**

**Windows:**
```bash
venv\Scripts\activate
```

You should see `(venv)` prefix in your terminal.

**macOS/Linux:**
```bash
source venv/bin/activate
```

#### **Step 4: Install Python Dependencies**

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Wait for installation to complete (usually 2-5 minutes).

#### **Step 5: Verify Installation**

```bash
python -c "import streamlit; import pytesseract; import pdf2image; print('All packages installed successfully!')"
```

---

### Phase 3: Windows-Specific Configuration (Optional)

If Tesseract is not in your PATH, edit `app.py` and add this line near the top:

```python
import pytesseract
pytesseract.pytesseract.pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

---

## Running the Application

### **Quick Start (Recommended)**

#### **Windows:**
Double-click `run.bat` in the project folder.

#### **macOS/Linux:**
```bash
chmod +x run.sh
./run.sh
```

### **Manual Start**

**Windows:**
```bash
venv\Scripts\activate
streamlit run app.py
```

**macOS/Linux:**
```bash
source venv/bin/activate
streamlit run app.py
```

### **Browser Access**

The application will automatically open at:
```
http://localhost:8501
```

If it doesn't open automatically, paste the URL in your browser.

---

## Troubleshooting Installation

### ❌ "Python not found"
**Solution:**
1. Ensure Python 3.8+ is installed: https://www.python.org/downloads/
2. During installation, check "Add Python to PATH"
3. Restart your terminal

### ❌ "Tesseract not found"
**Windows:**
```bash
# Verify installation
"C:\Program Files\Tesseract-OCR\tesseract.exe" --version
```

**macOS/Linux:**
```bash
which tesseract
```

### ❌ "pdf2image module not working"
**Solution:** Poppler not installed or not in PATH
- Reinstall Poppler
- Verify it's in your system PATH
- Restart terminal after adding to PATH

### ❌ "virtual environment activation fails"
**Windows - Try alternative:**
```bash
venv\Scripts\activate.bat
```

**macOS/Linux - Alternative:**
```bash
bash venv/bin/activate
```

### ❌ "pip install fails"
**Solution:**
```bash
# Upgrade pip
python -m pip install --upgrade pip

# Clear pip cache
pip cache purge

# Retry install
pip install -r requirements.txt
```

### ❌ "ModuleNotFoundError" when running app
1. Ensure virtual environment is activated (you should see `(venv)` in terminal)
2. Run: `pip install -r requirements.txt` again
3. Restart the application

### ❌ "Port 8501 already in use"
**Solution:**
```bash
streamlit run app.py --server.port 8502
```

---

## Post-Installation Verification

Create a test file to verify everything works:

1. Create `test_setup.py`:
```python
import pytesseract
from pdf2image import convert_from_path
from PyPDF2 import PdfReader
import streamlit
import reportlab

print("✓ Streamlit:", streamlit.__version__)
print("✓ Pytesseract: OK")
print("✓ PDF2Image: OK")
print("✓ PyPDF2: OK")
print("✓ Reportlab: OK")

# Test Tesseract
try:
    pytesseract.get_tesseract_version()
    print("✓ Tesseract OCR: OK")
except:
    print("✗ Tesseract OCR: NOT FOUND")

print("\nAll dependencies installed successfully!")
```

2. Run test:
```bash
python test_setup.py
```

---

## Creating a Shortcut (Windows)

For easier access, create a desktop shortcut:

1. Right-click on desktop → New → Shortcut
2. Location: `C:\Users\AHMED\ilovecoffee\run.bat`
3. Name: "PDF Marker"
4. Click Finish

Now you can double-click "PDF Marker" to start the application.

---

## First Test Run

### Test 1: With Sample Markscheme

1. Run the application
2. Upload any PDF as student answers
3. Upload `sample_markscheme.json` as markscheme
4. Set threshold to 50% (to see marking)
5. Click "Process and Mark"

### Test 2: With Your Own Files

1. Create a test PDF with answers (use Word, Google Docs, etc.)
2. Create matching markscheme in TXT, JSON, or PDF format
3. Upload both files
4. Verify results

---

## Performance Tips

- **First Run:** Tesseract will download language data (~100MB), this is normal
- **Large PDFs:** Process big documents in batches
- **Accuracy:** Better PDF quality = better OCR results

---

## Updating Dependencies

To update packages later:

```bash
# Activate virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Update all packages
pip install --upgrade -r requirements.txt
```

---

## Uninstalling

### Remove Virtual Environment
```bash
# Windows
rmdir /s venv

# macOS/Linux
rm -rf venv
```

### Remove Python Packages
If using fresh Python installation, you can skip this.

---

## Next Steps

1. ✅ Follow installation steps above
2. ✅ Run the application
3. ✅ Read QUICKSTART.md for first use
4. ✅ Test with sample files provided
5. ✅ Upload your own files and mark!

---

## Getting Help

1. Check README.md for detailed documentation
2. Review QUICKSTART.md for common issues
3. Verify all system dependencies are installed
4. Test with sample files first
5. Check internet connection (for first-time dependency downloads)

---

**Installation Complete!** 🎉

You're ready to use the Automated PDF Marking System. 

👉 Next: Run the application and check QUICKSTART.md

Questions? Review the documentation files or test with sample_markscheme.json
