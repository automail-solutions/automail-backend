from dataclasses import dataclass
from typing import Optional
from ..value_objects.category import EmailCategory


@dataclass
class Email:
    subject: str
    body: str
    sender: Optional[str] = None
    category: Optional[EmailCategory] = None
    confidence: Optional[float] = None
    suggested_response: Optional[str] = None