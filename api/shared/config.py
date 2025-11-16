from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    groq_api_key: str
    environment: str = "development"
    log_level: str = "INFO"
    allowed_origins: str = "*"
    
    @property
    def cors_origins(self) -> List[str]:
        return [origin.strip() for origin in self.allowed_origins.split(",")]
    
    class Config:
        env_file = ".env"


settings = Settings()