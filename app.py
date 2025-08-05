import streamlit as st
import PyPDF2
from summarizer import summarize_text
from summarizer import extract_keywords

# Set page config
st.set_page_config(page_title="AI PDF Summarizer", page_icon="📄", layout="centered")

# Custom CSS styling
st.markdown("""
    <style>
    .main {
        background-color: #f6f6f6;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 0.5em 1.5em;
        border-radius: 8px;
        border: none;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #45a049;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# App title
st.title("📄 AI PDF Summarizer")
st.subheader("Upload your PDF and get a clean, concise summary!")

# File uploader
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

# If a file is uploaded
if uploaded_file is not None:
    reader = PyPDF2.PdfReader(uploaded_file)
    raw_text = ""

    for page in reader.pages:
        raw_text += page.extract_text()

    if len(raw_text.strip()) == 0:
        st.error("No text could be extracted from this PDF.")
    else:
        summary_length = st.slider("Select Summary Length (approx. number of words)", 20, 200, 60)
        
        if st.button("🔍 Summarize"):
            with st.spinner("Summarizing your PDF..."):
                summary = summarize_text(raw_text, max_length=summary_length)

                st.markdown("### ✅ Summary:")
                st.success(summary)

                st.download_button("💾 Download Summary", summary, file_name="summary.txt")

                keywords = extract_keywords(raw_text)
                st.subheader("🔑 Extracted Keywords:")
                st.write(", ".join(keywords))

# Footer
st.markdown("---")
st.markdown("<center>Made with ❤️ using Streamlit & Hugging Face</center>", unsafe_allow_html=True)
