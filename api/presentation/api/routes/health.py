from fastapi import APIRouter
from ...schemas.response import HealthCheckResponse
from ....shared.utils import get_current_timestamp

router = APIRouter(tags=["Health"])


@router.get(
    "/health",
    response_model=HealthCheckResponse,
    summary="Verifica saúde da aplicação",
    description="Retorna o status atual da aplicação e informações de versão"
)
async def health_check():
    """Endpoint de health check para monitoramento da aplicação."""
    return HealthCheckResponse(
        status="healthy",
        version="1.0.0",
        timestamp=get_current_timestamp()
    )