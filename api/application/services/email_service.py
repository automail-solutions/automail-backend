import time
from ...domain.entities.email import Email
from ...domain.value_objects.category import EmailCategory
from ...infrastructure.ai.groq_client import GroqClient
from ...infrastructure.nlp.text_processor import TextProcessor


class EmailService:
    def __init__(self):
        self.groq_client = GroqClient()
        self.text_processor = TextProcessor()
    
    async def classify_email(self, subject: str, body: str, sender: str = None) -> tuple[Email, float]:
        start_time = time.time()
        
        # Preprocess text
        clean_subject, clean_body = self.text_processor.preprocess_email(subject, body)
        
        # Classify with AI
        category_str, confidence, suggested_response = await self.groq_client.classify_and_respond(
            clean_subject, clean_body
        )
        
        # Convert to enum
        category = EmailCategory.PRODUCTIVE if category_str == "Produtivo" else EmailCategory.UNPRODUCTIVE
        
        # Create email entity
        email = Email(
            subject=subject,
            body=body,
            sender=sender,
            category=category,
            confidence=confidence,
            suggested_response=suggested_response
        )
        
        processing_time = time.time() - start_time
        return email, processing_time