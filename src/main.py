from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from .presentation.api.routes import classify, health, batch_classify
from .shared.config import settings
from .shared.exceptions import AutomailException

# FastAPI app with detailed metadata for Swagger
app = FastAPI(
    title="Automail Solutions API",
    description="API stateless para classificação automática de emails e sugestão de respostas usando IA",
    version="1.0.0",
    contact={
        "name": "Automail Solutions Team"
    },
    openapi_tags=[
        {
            "name": "Classification",
            "description": "Endpoints de classificação de emails (processamento em tempo real)"
        },
        {
            "name": "Health",
            "description": "Endpoints de monitoramento"
        }
    ]
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(classify.router)
app.include_router(batch_classify.router)
app.include_router(health.router)

# Global exception handler
@app.exception_handler(AutomailException)
async def automail_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc)}
    )

# Root endpoint
@app.get("/", include_in_schema=False)
async def root():
    return {"message": "Automail Solutions API - Acesse /docs para documentação"}

# For Vercel deployment
handler = app