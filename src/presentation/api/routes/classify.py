from fastapi import APIRouter, Depends, HTTPException
from ...schemas.request import EmailClassificationRequest
from ...schemas.response import EmailClassificationResponse, ErrorResponse
from ...api.dependencies import get_classify_email_use_case
from ....application.use_cases.classify_email import ClassifyEmailUseCase
from ....shared.exceptions import AIServiceError, ClassificationError
from ....shared.utils import create_metadata

router = APIRouter(tags=["Classification"])


@router.post(
    "/api/v1/classify",
    response_model=EmailClassificationResponse,
    summary="Classifica um email e sugere resposta",
    description="Recebe o conteúdo de um email e retorna a classificação (Produtivo/Improdutivo) com uma sugestão de resposta automática. Processamento em tempo real sem armazenamento.",
    responses={
        200: {"description": "Classificação realizada com sucesso"},
        400: {"description": "Dados de entrada inválidos", "model": ErrorResponse},
        500: {"description": "Erro interno do servidor", "model": ErrorResponse}
    }
)
async def classify_email(
    request: EmailClassificationRequest,
    use_case: ClassifyEmailUseCase = Depends(get_classify_email_use_case)
):
    """
    Classifica um email em Produtivo ou Improdutivo e sugere uma resposta automática.
    
    - **Produtivo**: Emails que requerem ação (suporte, dúvidas, solicitações)
    - **Improdutivo**: Emails sociais (felicitações, agradecimentos)
    """
    try:
        email, processing_time = await use_case.execute(
            subject=request.email_subject,
            body=request.email_body,
            sender=request.sender
        )
        
        return EmailClassificationResponse(
            category=email.category.value,
            confidence=email.confidence,
            suggested_response=email.suggested_response,
            metadata=create_metadata(processing_time)
        )
        
    except (AIServiceError, ClassificationError) as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro interno do servidor")