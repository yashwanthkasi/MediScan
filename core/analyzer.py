from services.file_processor import FileProcessor
from services.llm_service import LLMService
from models.report import Report

class Analyzer:
    def __init__(self):
        self.file_processor = FileProcessor()
        self.llm_service = LLMService()

    def process_report(self, file):
        # Extract text from the file (PDF or Image)
        text = self.file_processor.extract_text(file)
        
        # Clean and preprocess text
        report_text = Report(text).clean_text()
        
        # Analyze report using LLM
        analysis = self.llm_service.analyze_report(report_text)
        return analysis
