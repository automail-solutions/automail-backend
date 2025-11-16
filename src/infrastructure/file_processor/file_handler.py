import io
from fastapi import UploadFile, HTTPException
import PyPDF2


class FileHandler:
    MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
    ALLOWED_EXTENSIONS = {'.txt', '.pdf'}
    
    @staticmethod
    def validate_file(file: UploadFile) -> None:
        if not file.filename:
            raise HTTPException(status_code=400, detail="Nome do arquivo é obrigatório")
        
        extension = '.' + file.filename.split('.')[-1].lower()
        if extension not in FileHandler.ALLOWED_EXTENSIONS:
            raise HTTPException(status_code=400, detail=f"Formato não suportado. Use: {', '.join(FileHandler.ALLOWED_EXTENSIONS)}")
    
    @staticmethod
    async def extract_text(file: UploadFile) -> str:
        FileHandler.validate_file(file)
        
        content = await file.read()
        
        if len(content) > FileHandler.MAX_FILE_SIZE:
            raise HTTPException(status_code=400, detail="Arquivo muito grande. Máximo 5MB")
        
        if len(content) == 0:
            raise HTTPException(status_code=400, detail="Arquivo vazio")
        
        try:
            extension = '.' + file.filename.split('.')[-1].lower()
            
            if extension == '.txt':
                text = content.decode('utf-8')
            elif extension == '.pdf':
                text = FileHandler._extract_pdf_text(content)
            
            if not text or not text.strip():
                raise HTTPException(status_code=400, detail="Arquivo não contém texto válido")
            
            return text.strip()
            
        except UnicodeDecodeError:
            raise HTTPException(status_code=400, detail="Arquivo corrompido ou codificação inválida")
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Erro ao processar arquivo: {str(e)}")
    
    @staticmethod
    def _extract_pdf_text(content: bytes) -> str:
        try:
            pdf_reader = PyPDF2.PdfReader(io.BytesIO(content))
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
        except Exception:
            raise HTTPException(status_code=400, detail="PDF corrompido ou protegido")