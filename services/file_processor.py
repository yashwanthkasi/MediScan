import PyPDF2
from PIL import Image
import pytesseract

class FileProcessor:
    def extract_text(self, file):
        if file.type == "application/pdf":
            return self._extract_text_from_pdf(file)
        else:
            return self._extract_text_from_image(file)

    def _extract_text_from_pdf(self, pdf_file):
        # Use PdfReader instead of PdfFileReader
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""

        # Iterate through each page
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        return text

    def _extract_text_from_image(self, image_file):
        img = Image.open(image_file)
        text = pytesseract.image_to_string(img)
        return text
