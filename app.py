import streamlit as st
from core.analyzer import Analyzer
from core.qna import QnA
import os
from dotenv import load_dotenv
load_dotenv()

st.title("Medical Report Analyzer")

# File uploader for PDF/Image
uploaded_file = st.file_uploader("Upload a medical report (PDF or Image)", type=["pdf", "png", "jpg", "jpeg"])

if uploaded_file:
    analyzer = Analyzer()
    
    # Process the report
    analysis = analyzer.process_report(uploaded_file)
    
    # Display initial analysis
    st.write("Medical Report Analysis:")
    st.write(analysis)

    # Interactive Q&A
    question = st.text_input("Ask a question about the report:")
    if question:
        qna = QnA(analysis)
        answer = qna.ask_question(question)
        st.write("Answer:")
        st.write(answer)
