from pydantic import BaseModel, Field
from typing import Dict, Any, List, Union


class EmailClassificationResponse(BaseModel):
    category: str = Field(
        description="Categoria do email",
        examples=["Produtivo", "Improdutivo"]
    )
    confidence: float = Field(
        description="Confiança da classificação (0-1)",
        examples=[0.95, 0.87]
    )
    suggested_response: str = Field(
        description="Resposta sugerida para o email",
        examples=[
            "Obrigado pelo contato. Nossa equipe técnica irá analisar sua solicitação.",
            "Obrigado pelas felicitações! Desejamos um feliz natal para você também!"
        ]
    )
    metadata: Dict[str, Any] = Field(
        description="Metadados do processamento",
        examples=[{
            "processing_time": 1.23,
            "timestamp": "2025-01-02 10:30:45"
        }]
    )


class HealthCheckResponse(BaseModel):
    status: str = Field(description="Status da aplicação", examples=["healthy"])
    version: str = Field(description="Versão da aplicação", examples=["1.0.0"])
    timestamp: str = Field(description="Timestamp da verificação", examples=["2025-01-02 10:30:45"])


class ErrorResponse(BaseModel):
    detail: str = Field(description="Detalhes do erro", examples=["Erro interno do servidor"])


class BatchFileResult(BaseModel):
    filename: str = Field(description="Nome do arquivo processado")
    status: str = Field(description="Status do processamento", examples=["success", "error"])
    category: Union[str, None] = Field(default=None, description="Categoria do email")
    confidence: Union[float, None] = Field(default=None, description="Confiança da classificação")
    suggested_response: Union[str, None] = Field(default=None, description="Resposta sugerida")
    processing_time: Union[float, None] = Field(default=None, description="Tempo de processamento")
    error: Union[str, None] = Field(default=None, description="Mensagem de erro")


class BatchClassificationResponse(BaseModel):
    total_files: int = Field(description="Total de arquivos processados")
    successful: int = Field(description="Arquivos processados com sucesso")
    failed: int = Field(description="Arquivos com erro")
    results: List[BatchFileResult] = Field(description="Resultados detalhados")
    metadata: Dict[str, Any] = Field(description="Metadados do processamento")