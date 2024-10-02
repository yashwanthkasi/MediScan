from services.llm_service import LLMService
class QnA:
    def __init__(self, report_text):
        self.report_text = report_text
        self.llm_service = LLMService()

    def ask_question(self, question):
        # Create a contextual question prompt
        prompt = f"The medical report is:\n{self.report_text}\nThe question is: {question}"
        answer = self.llm_service.ask_question(prompt)
        return answer
