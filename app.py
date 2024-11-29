import streamlit as st
from services.file_uploader import extract_pdf_text
from services.youtube_extractor import extract_youtube_text
from core.question_generator import generate_questions

# Page Configurations
st.set_page_config(
    page_title="Study Better App",
    page_icon="📘",
    layout="wide"
)

def main():
    st.title("📘 Study Better App")
    st.write("Upload a PDF or provide a YouTube video link to test your knowledge with AI-generated questions.")

    # Sidebar Options
    with st.sidebar:
        option = st.radio(
            "Choose your input type:",
            options=["PDF Upload", "YouTube Link"]
        )

    # File Upload Section
    if option == "PDF Upload":
        pdf_file = st.file_uploader("Upload your PDF file here", type="pdf")
        if pdf_file:
            with st.spinner("Extracting text from PDF..."):
                pdf_text = extract_pdf_text(pdf_file)
                if pdf_text:
                    process_and_display(pdf_text)
                else:
                    st.error("Could not extract text. Please upload a valid PDF.")
    
    # YouTube Link Section
    elif option == "YouTube Link":
        youtube_url = st.text_input("Paste YouTube video link here")
        if youtube_url:
            with st.spinner("Extracting text from YouTube video..."):
                youtube_text = extract_youtube_text(youtube_url)
                if youtube_text:
                    process_and_display(youtube_text)
                else:
                    st.error("Could not extract text. Please provide a valid YouTube link.")

def process_and_display(text: str):
    """Process text and display generated questions."""
    st.write("### Extracted Content")
    st.write(text[:1000] + "..." if len(text) > 1000 else text)  # Truncate long text for display
    
    with st.spinner("Generating questions..."):
        questions = generate_questions(text)
        if questions:
            st.write("### Generated Questions")
            for i, question in enumerate(questions, 1):
                st.write(f"**Q{i}:** {question}")
        else:
            st.error("Could not generate questions. Please try again.")

if __name__ == "__main__":
    main()
