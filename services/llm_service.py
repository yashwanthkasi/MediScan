from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
import os

class LLMService:
    def __init__(self):
        self.llm = ChatGroq(
            model="llama-3.1-70b-versatile",
            groq_api_key=os.getenv('GROQ_API_KEY'),
            temperature = 0.1
        )
        self.prompt = PromptTemplate.from_template("""
        You are a medical expert. Given the following medical report, analyze and summarize the important findings:
        {report}

        Provide a detailed explanation, including diagnosis, medications, and recommendations.
        """
        )

    def analyze_report(self, report_text):
        chain_extract = self.prompt | self.llm
        res = chain_extract.invoke(input={'report': report_text})
        return res.content

    def ask_question(self, prompt):
        return self.llm(prompt)
