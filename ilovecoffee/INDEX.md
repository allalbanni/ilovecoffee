# 📖 Getting Started - Read This First!

Welcome to the **Automated PDF Marking System**! This guide will help you navigate the project files and get started quickly.

## 🎯 What This System Does

This application automatically:
1. ✅ Reads student answer PDFs
2. ✅ Extracts text using OCR (Optical Character Recognition)
3. ✅ Compares answers with a markscheme
4. ✅ Generates corrected PDFs and detailed feedback

Perfect for educators, tutors, and exam boards!

---

## 📚 Documentation Files (Read in Order)

### 1️⃣ **START HERE: QUICKSTART.md** (5 minutes)
- Quick setup instructions
- First-time user guide
- Common troubleshooting

👉 **Read this if:** You want to get running quickly

### 2️⃣ **INSTALLATION.md** (20 minutes)
- Detailed step-by-step installation
- System dependency setup
- Verification & testing

👉 **Read this if:** You need help installing or encounter errors

### 3️⃣ **README.md** (Complete Reference)
- Full documentation
- All features explained
- Markscheme format examples
- Advanced configuration

👉 **Read this if:** You want comprehensive information

### 4️⃣ **PROJECT_SUMMARY.md** (Technical Overview)
- Architecture overview
- File structure explanation
- Technology stack
- Deployment options

👉 **Read this if:** You want to understand how it works or extend it

### 5️⃣ **This File** (You are here!)
- Navigation guide
- Quick reference
- File descriptions

---

## 🚀 Quick Start (3 Steps)

### Step 1: Setup (One-time)
```bash
# Windows: Double-click run.bat
# OR
# macOS/Linux: bash ./run.sh
```

### Step 2: Upload Files
- Student answer PDF
- Markscheme (TXT, JSON, or PDF)

### Step 3: Mark & Download
- Click "Process and Mark"
- Get your corrected PDFs!

---

## 📁 Project Files Explained

### 🔴 **Must Have Files** (Keep these)

| File | Purpose |
|------|---------|
| `app.py` | Main application (do not edit unless you know Python) |
| `pdf_processor.py` | PDF handling (do not edit unless you know Python) |
| `marking_engine.py` | Marking logic (do not edit unless you know Python) |
| `requirements.txt` | Dependencies list |

### 🟡 **Configuration Files** (Customize if needed)

| File | Purpose |
|------|---------|
| `config.ini` | Settings (optional) |
| `run.bat` | Windows startup script |
| `run.sh` | macOS/Linux startup script |

### 🟢 **Sample & Reference Files** (For testing)

| File | Purpose |
|------|---------|
| `sample_markscheme.json` | Example markscheme (JSON format) |
| `sample_markscheme.txt` | Example markscheme (text format) |

### 🔵 **Documentation Files** (For reference)

| File | Purpose |
|------|---------|
| `README.md` | Complete documentation |
| `QUICKSTART.md` | 5-minute setup guide |
| `INSTALLATION.md` | Detailed installation |
| `PROJECT_SUMMARY.md` | Technical overview |
| `INDEX.md` | This file |

---

## 💡 Common Questions

### Q: "Where do I start?"
**A:** Follow this order:
1. Read QUICKSTART.md
2. Run run.bat (Windows) or run.sh (Mac/Linux)
3. Upload files and test

### Q: "I'm getting an error"
**A:** Check INSTALLATION.md troubleshooting section

### Q: "What markscheme formats work?"
**A:** JSON, plain text, or PDF. See README.md for examples.

### Q: "Can I customize the marking?"
**A:** Yes! Edit `config.ini` or the code in `marking_engine.py`

### Q: "How accurate is the OCR?"
**A:** Depends on PDF quality. Test with sample files first.

---

## 🎯 Next Steps

### Choose Your Path:

**🟢 I'm Ready to Get Started:**
1. Open QUICKSTART.md
2. Follow the 3-step setup
3. Test with sample files

**🟡 I Need Help Installing:**
1. Open INSTALLATION.md
2. Follow system-specific instructions
3. Use troubleshooting section if needed

**🔵 I Want Full Documentation:**
1. Open README.md
2. Read "Usage" section
3. Try examples provided

**⚫ I'm a Developer/Want to Extend:**
1. Open PROJECT_SUMMARY.md
2. Understand architecture
3. Modify Python files as needed

---

## 🔧 System Requirements

- **OS:** Windows, macOS, or Linux
- **Python:** 3.8+ (https://www.python.org)
- **Dependencies:** Auto-installed by `run.bat` or `run.sh`
- **Space:** ~500MB for dependencies

---

## 📊 Feature Comparison

| Feature | Support |
|---------|---------|
| Student PDF Upload | ✅ Yes |
| Markscheme Formats | ✅ JSON, TXT, PDF |
| OCR Extraction | ✅ Yes (English default) |
| Marking Modes | ✅ Strict, Flexible, Keyword |
| Batch Processing | 🔶 Single file (easily extended) |
| Web Interface | ✅ Yes (Streamlit) |
| Export Formats | ✅ PDF, Feedback Report |
| User Authentication | ❌ No (local use only) |

---

## 🎓 Educational Use Cases

Perfect for:
- ✅ MCQ marking
- ✅ Short answer grading
- ✅ Exam paper evaluation
- ✅ Assignment checking
- ✅ Test paper marking

---

## 🔒 Privacy & Security

- **Local Processing:** Files never leave your computer
- **No Cloud Upload:** Everything runs locally
- **Temporary Files:** Cleaned up automatically
- **Offline Capable:** Works without internet

---

## 🎯 Pro Tips

1. **Better Results:** Use clear, high-quality PDF scans
2. **Accurate Markscheme:** Write clear, specific expected answers
3. **Test First:** Try with sample files before real data
4. **Adjust Settings:** Lower threshold for partial credit

---

## 📞 Troubleshooting Quick Links

- ❌ "Tesseract not found" → See INSTALLATION.md
- ❌ "No module named 'streamlit'" → See QUICKSTART.md
- ❌ "PDF extraction fails" → See README.md > Troubleshooting
- ❌ "Poor OCR results" → See README.md > Advanced Features

---

## 📈 What's Next?

### After First Success:
1. Test with your own answer PDFs
2. Create custom markschemes
3. Adjust marking thresholds
4. Experiment with different modes

### Advanced (Optional):
1. Modify `marking_engine.py` for custom logic
2. Add database storage
3. Create batch processing
4. Deploy to cloud server

---

## 🚀 Command Reference

```bash
# Startup
run.bat                    # Windows
./run.sh                   # macOS/Linux

# Manual startup
streamlit run app.py       # After activating venv

# Different port
streamlit run app.py --server.port 8502

# Check dependencies
python test_setup.py

# Update packages
pip install --upgrade -r requirements.txt
```

---

## 📞 Support Resources

1. **Quick Issues:** Check README.md troubleshooting
2. **Setup Issues:** Check INSTALLATION.md
3. **First Time:** Read QUICKSTART.md
4. **Technical:** Read PROJECT_SUMMARY.md

---

## ✅ Checklist Before Starting

- [ ] Python 3.8+ installed?
- [ ] Tesseract OCR installed?
- [ ] Poppler installed?
- [ ] Have test PDF & markscheme files?
- [ ] Read QUICKSTART.md?
- [ ] Ready to launch?

---

## 🎉 You're Ready!

Choose your next step:

👉 **New User?** → Open QUICKSTART.md

👉 **Need Installation Help?** → Open INSTALLATION.md

👉 **Want Full Details?** → Open README.md

👉 **Ready to Start?** → Run `run.bat` (Windows) or `./run.sh` (Mac/Linux)

---

**Happy Marking!** 📝✨

Questions? Check the relevant documentation file above.

---

*Last Updated: May 2026*  
*Version: 1.0*  
*Status: Ready to Use*
