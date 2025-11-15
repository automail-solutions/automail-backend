from pydantic import BaseModel, Field, field_validator
from typing import Optional


class EmailClassificationRequest(BaseModel):
    email_subject: str = Field(
        description="Assunto do email",
        examples=["Dúvida sobre o sistema", "Feliz Natal!"]
    )
    email_body: str = Field(
        description="Corpo do email",
        examples=[
            "Estou com dificuldades para acessar o sistema. Podem me ajudar?",
            "Desejo um feliz natal para toda a equipe!"
        ]
    )
    
    @field_validator('email_body')
    @classmethod
    def validate_email_body(cls, v):
        if not v or not v.strip():
            raise ValueError('O corpo do email não pode estar vazio')
        return v
    sender: Optional[str] = Field(
        default=None,
        description="Remetente do email (opcional)",
        examples=["cliente@empresa.com"]
    )