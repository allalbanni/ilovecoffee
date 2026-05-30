"""
Automated PDF Marking System - Streamlit Web Application
Extracts student answers from PDF, compares with markscheme, and generates corrected PDFs
"""

try:
    import streamlit as st
except Exception as e:
    raise ImportError("streamlit is required to run this app. Install it with `pip install streamlit`.") from e
import tempfile
import os
import json
from pdf_processor import PDFProcessor
from marking_engine import MarkingEngine

# Page configuration
st.set_page_config(
    page_title="Automated PDF Marker",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .stTabs [data-baseweb="tab-list"] button {
        font-size: 18px;
    }
    .success-box {
        padding: 15px;
        border-radius: 5px;
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
    }
    .error-box {
        padding: 15px;
        border-radius: 5px;
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📝 Automated PDF Marking System")
st.write("Upload student answers and a markscheme to automatically mark and generate a corrected PDF")

# Sidebar for instructions
with st.sidebar:
    st.header("Instructions")
    st.markdown("""
    ### How to Use:
    1. **Upload Files**: Provide the student answer PDF and markscheme
    2. **Configure**: Set marking parameters (if needed)
    3. **Mark**: The system will automatically extract and compare answers
    4. **Download**: Get both annotated and feedback PDFs
    
    ### Supported Formats:
    - **Student Answers**: PDF files
    - **Markscheme**: Text files, PDF, or JSON format
    
    ### Features:
    - ✓ OCR text extraction
    - ✓ Automatic answer comparison
    - ✓ Annotated PDF with corrections
    - ✓ Detailed feedback report
    """)

# Main application
tab1, tab2, tab3 = st.tabs(["Upload", "Configure", "Results"])

with tab1:
    st.header("Step 1: Upload Your Files")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Student Answer Sheet")
        student_pdf = st.file_uploader(
            "Upload the student's answer PDF",
            type=["pdf"],
            key="student_pdf"
        )
        if student_pdf:
            st.success(f"✓ Uploaded: {student_pdf.name}")
    
    with col2:
        st.subheader("Markscheme")
        markscheme_file = st.file_uploader(
            "Upload the markscheme (PDF, TXT, or JSON)",
            type=["pdf", "txt", "json"],
            key="markscheme"
        )
        if markscheme_file:
            st.success(f"✓ Uploaded: {markscheme_file.name}")

with tab2:
    st.header("Step 2: Configuration Settings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        matching_threshold = st.slider(
            "Matching Threshold (%)",
            min_value=0,
            max_value=100,
            value=80,
            help="Minimum similarity percentage to consider an answer correct"
        )
    
    with col2:
        ignore_case = st.checkbox(
            "Ignore Case",
            value=True,
            help="Treat uppercase and lowercase as identical"
        )
    
    st.divider()
    
    st.subheader("Marking Mode")
    marking_mode = st.radio(
        "How should answers be marked?",
        ["Strict (Exact Match)", "Flexible (Similarity-Based)", "Keyword-Based"],
        help="Choose how strict the marking should be"
    )
    mode_map = {
        "Strict (Exact Match)": "strict",
        "Flexible (Similarity-Based)": "flexible",
        "Keyword-Based": "keyword"
    }

with tab3:
    st.header("Step 3: Mark and Generate Results")
    
    if student_pdf is None or markscheme_file is None:
        st.warning("⚠️ Please upload both files in the Upload tab first")
    else:
        if st.button("🔍 Process and Mark", use_container_width=True, type="primary"):
            with st.spinner("Processing PDF..."):
                try:
                    # Create temporary directory for file handling
                    tmpdir = tempfile.mkdtemp()
                    student_pdf_path = os.path.join(tmpdir, "student.pdf")
                    markscheme_ext = os.path.splitext(markscheme_file.name)[1].lower().lstrip('.')
                    markscheme_path = os.path.join(tmpdir, f"markscheme.{markscheme_ext}")

                    with open(student_pdf_path, "wb") as f:
                        f.write(student_pdf.getbuffer())

                    with open(markscheme_path, "wb") as f:
                        f.write(markscheme_file.getbuffer())

                    # Initialize processors
                    st.write("📄 Extracting student answers...")
                    pdf_processor = PDFProcessor()
                    student_text = pdf_processor.extract_text_from_pdf(student_pdf_path)
                    st.write(f"✓ Extracted {len(student_text)} characters from student PDF")

                    st.write("📋 Parsing markscheme...")
                    if markscheme_ext == "pdf":
                        markscheme_text = pdf_processor.extract_text_from_pdf(markscheme_path)
                    elif markscheme_ext == "json":
                        with open(markscheme_path, 'r', encoding='utf-8') as f:
                            markscheme_text = json.load(f)
                    else:  # txt
                        with open(markscheme_path, 'r', encoding='utf-8') as f:
                            markscheme_text = f.read()

                    st.write(f"✓ Loaded markscheme ({len(str(markscheme_text))} characters)")

                    # Initialize marking engine
                    marking_engine = MarkingEngine(
                        threshold=matching_threshold / 100,
                        ignore_case=ignore_case,
                        mode=mode_map.get(marking_mode, "strict")
                    )

                    st.write("✏️ Comparing answers...")
                    results = marking_engine.mark_answers(student_text, markscheme_text)

                    st.write("📄 Generating marked PDF...")
                    annotated_pdf = pdf_processor.annotate_pdf(student_pdf_path, results)
                    annotated_pdf_path = os.path.join(tmpdir, "marked_annotated.pdf")
                    with open(annotated_pdf_path, "wb") as f:
                        f.write(annotated_pdf.getvalue())

                    st.write("📊 Generating feedback report...")
                    feedback_pdf_path = os.path.join(tmpdir, "feedback_report.pdf")
                    pdf_processor.generate_feedback_pdf(results, feedback_pdf_path)

                    # Store results in session state
                    st.session_state.results = results
                    st.session_state.annotated_pdf_path = annotated_pdf_path
                    st.session_state.feedback_pdf_path = feedback_pdf_path
                    st.session_state.marking_complete = True
                    st.session_state.temp_dir = tmpdir

                    st.success("✓ Marking complete!")
                
                except Exception as e:
                    st.error(f"❌ Error during processing: {str(e)}")
                    st.error("Please check that your files are valid and try again.")
        
        # Display results if available
        if "marking_complete" in st.session_state and st.session_state.marking_complete:
            st.divider()
            st.header("📊 Results")
            
            results = st.session_state.results
            
            # Summary statistics
            col1, col2, col3, col4 = st.columns(4)
            
            total_questions = results.get("total_questions", 0)
            correct_answers = results.get("correct_answers", 0)
            score_percentage = results.get("score_percentage", 0)
            
            with col1:
                st.metric("Total Questions", total_questions)
            with col2:
                st.metric("Correct Answers", correct_answers)
            with col3:
                st.metric("Score", f"{score_percentage:.1f}%")
            with col4:
                st.metric("Incorrect", total_questions - correct_answers)
            
            st.divider()
            
            # Display detailed feedback
            st.subheader("Detailed Feedback")
            if "questions" in results:
                for i, question in enumerate(results["questions"], 1):
                    with st.expander(f"Question {i}: {question.get('status', 'Pending').upper()}"):
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.write("**Student Answer:**")
                            st.code(question.get("student_answer", "N/A"))
                        
                        with col2:
                            st.write("**Correct Answer:**")
                            st.code(question.get("expected_answer", "N/A"))
                        
                        st.write("**Feedback:**")
                        st.info(question.get("feedback", "No feedback available"))
                        
                        if "similarity" in question:
                            st.write(f"Similarity Score: {question['similarity']*100:.1f}%")
            
            st.divider()
            
            # Download section
            st.subheader("📥 Download Results")
            
            col1, col2 = st.columns(2)
            
            with col1:
                with open(st.session_state.annotated_pdf_path, "rb") as f:
                    st.download_button(
                        label="📄 Download Annotated PDF",
                        data=f.read(),
                        file_name="marked_answers_annotated.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )
            
            with col2:
                with open(st.session_state.feedback_pdf_path, "rb") as f:
                    st.download_button(
                        label="📊 Download Feedback Report",
                        data=f.read(),
                        file_name="feedback_report.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )

st.divider()
st.caption("🔒 Your files are processed locally and not stored. Reset the page to start over.")
