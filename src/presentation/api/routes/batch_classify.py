import time
from typing import List
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from ...schemas.response import BatchClassificationResponse, ErrorResponse
from ...api.dependencies import get_batch_classify_emails_use_case
from ....application.use_cases.batch_classify_emails import BatchClassifyEmailsUseCase
from ....shared.utils import create_metadata

router = APIRouter(tags=["Classification"])


@router.post(
    "/api/v1/classify/batch",
    response_model=BatchClassificationResponse,
    summary="Classifica múltiplos emails de arquivos",
    description="Recebe arquivos .txt ou .pdf contendo emails e retorna classificação em lote. Máximo 5MB por arquivo.",
    responses={
        200: {"description": "Classificação em lote realizada"},
        400: {"description": "Erro de validação de arquivos", "model": ErrorResponse},
        500: {"description": "Erro interno do servidor", "model": ErrorResponse}
    }
)
async def batch_classify_emails(
    files: List[UploadFile] = File(..., description="Arquivos de email (.txt ou .pdf)"),
    use_case: BatchClassifyEmailsUseCase = Depends(get_batch_classify_emails_use_case)
):
    """
    Processa múltiplos arquivos de email e retorna classificação para cada um.
    
    - **Formatos suportados**: .txt, .pdf
    - **Tamanho máximo**: 5MB por arquivo
    - **Validações**: formato, tamanho, conteúdo, corrupção
    """
    if not files:
        raise HTTPException(status_code=400, detail="Nenhum arquivo enviado")
    
    if len(files) > 10:
        raise HTTPException(status_code=400, detail="Máximo 10 arquivos por requisição")
    
    start_time = time.time()
    
    try:
        results = await use_case.execute(files)
        
        successful = sum(1 for r in results if r["status"] == "success")
        failed = len(results) - successful
        processing_time = time.time() - start_time
        
        return BatchClassificationResponse(
            total_files=len(results),
            successful=successful,
            failed=failed,
            results=results,
            metadata=create_metadata(processing_time)
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro interno do servidor")