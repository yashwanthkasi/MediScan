import re

def clean_text(text):
    # Remove unwanted characters, noise, etc.
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\d+', '', text)
    return text.strip()
