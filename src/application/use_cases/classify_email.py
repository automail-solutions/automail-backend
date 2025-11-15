from ..services.email_service import EmailService
from ...domain.entities.email import Email


class ClassifyEmailUseCase:
    def __init__(self, email_service: EmailService):
        self.email_service = email_service
    
    async def execute(self, subject: str, body: str, sender: str = None) -> tuple[Email, float]:
        return await self.email_service.classify_email(subject, body, sender)