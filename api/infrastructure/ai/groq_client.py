from groq import Groq
from typing import Tuple
from ...shared.config import settings
from ...shared.exceptions import AIServiceError


class GroqClient:
    def __init__(self):
        self.client = Groq(api_key=settings.groq_api_key)
    
    async def classify_and_respond(self, subject: str, body: str) -> Tuple[str, float, str]:
        try:
            prompt = f"""
            Classifique este email como "Produtivo" ou "Improdutivo" e sugira uma resposta.
            
            Produtivo: emails que requerem ação (suporte, dúvidas, solicitações)
            Improdutivo: emails sociais (felicitações, agradecimentos)
            
            Assunto: {subject}
            Corpo: {body}
            
            Responda no formato:
            Categoria: [Produtivo/Improdutivo]
            Confiança: [0.0-1.0]
            Resposta: [sugestão de resposta]
            """
            
            response = self.client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama-3.1-8b-instant",
                temperature=0.1
            )
            
            content = response.choices[0].message.content
            lines = content.strip().split('\n')
            
            category = "Produtivo"
            confidence = 0.8
            suggested_response = "Obrigado pelo contato."
            
            for line in lines:
                if line.startswith("Categoria:"):
                    category = line.split(': ', 1)[1].strip()
                elif line.startswith("Confiança:"):
                    try:
                        confidence = float(line.split(': ', 1)[1].strip())
                    except:
                        confidence = 0.8
                elif line.startswith("Resposta:"):
                    # Captura toda a resposta, incluindo múltiplas linhas
                    response_start = content.find("Resposta:")
                    if response_start != -1:
                        suggested_response = content[response_start + 10:].strip()
                    break
            
            return category, confidence, suggested_response
            
        except Exception as e:
            raise AIServiceError(f"Erro na classificação: {str(e)}")