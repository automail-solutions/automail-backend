import re


class TextProcessor:
    @staticmethod
    def clean_text(text: str) -> str:
        # Remove HTML tags
        text = re.sub(r'<[^>]+>', '', text)
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        # Remove special characters but keep basic punctuation
        text = re.sub(r'[^\w\s.,!?-]', '', text)
        return text.strip()
    
    @staticmethod
    def preprocess_email(subject: str, body: str) -> tuple[str, str]:
        clean_subject = TextProcessor.clean_text(subject)
        clean_body = TextProcessor.clean_text(body)
        return clean_subject, clean_body