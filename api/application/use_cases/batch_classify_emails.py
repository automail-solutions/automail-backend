from typing import List, Dict, Any
from ..services.email_service import EmailService
from ...infrastructure.file_processor.file_handler import FileHandler
from fastapi import UploadFile


class BatchClassifyEmailsUseCase:
    def __init__(self, email_service: EmailService):
        self.email_service = email_service
        self.file_handler = FileHandler()
    
    async def execute(self, files: List[UploadFile]) -> List[Dict[str, Any]]:
        results = []
        
        for file in files:
            try:
                # Extract text from file
                text = await self.file_handler.extract_text(file)
                print(f"Extracted text from {file.filename}: {text}...")  # Debugging line
                
                # Use first line as subject, rest as body
                lines = text.split('\n', 1)
                subject = lines[0][:100] if lines else "Email sem assunto"
                body = lines[1] if len(lines) > 1 else lines[0]
                
                # Classify email
                email, processing_time = await self.email_service.classify_email(subject, body)
                print(f"Suggested response for {file.filename}: {email.suggested_response}")

                results.append({
                    "filename": file.filename,
                    "status": "success",
                    "category": email.category.value,
                    "confidence": email.confidence,
                    "suggested_response": email.suggested_response,
                    "processing_time": processing_time
                })
                
            except Exception as e:
                results.append({
                    "filename": file.filename,
                    "status": "error",
                    "error": str(e)
                })
        
        return results