from fastapi import FastAPI
from app.api.routes import router
from app.config import settings

app = FastAPI(
    title="Financial Insight Engine",
    version="1.1.0",
    description="API service for financial insight workflows.",
)

app.include_router(router)


@app.get("/health", tags=["Health"])
def health():
    return {
        "status": "ok",
        "env": settings.APP_ENV,
        "service": "financial_insight_api",
        "version": "1.1.0"
    }