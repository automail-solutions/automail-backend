from ...application.services.email_service import EmailService
from ...application.use_cases.classify_email import ClassifyEmailUseCase
from ...application.use_cases.batch_classify_emails import BatchClassifyEmailsUseCase


def get_email_service() -> EmailService:
    return EmailService()


def get_classify_email_use_case() -> ClassifyEmailUseCase:
    email_service = get_email_service()
    return ClassifyEmailUseCase(email_service)


def get_batch_classify_emails_use_case() -> BatchClassifyEmailsUseCase:
    email_service = get_email_service()
    return BatchClassifyEmailsUseCase(email_service)