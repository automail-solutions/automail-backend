class AutomailException(Exception):
    pass


class ClassificationError(AutomailException):
    pass


class AIServiceError(AutomailException):
    pass