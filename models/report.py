from utils.text_cleaner import clean_text

class Report:
    def __init__(self, raw_text):
        self.raw_text = raw_text
        self.cleaned_text = None

    def clean_text(self):
        self.cleaned_text = clean_text(self.raw_text)
        return self.cleaned_text
