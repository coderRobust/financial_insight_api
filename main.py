from fastapi import FastAPI
from app.api.routes import router
from app.config import settings

app = FastAPI(title="Financial Insight Engine")

app.include_router(router)


@app.get("/health")
def health():
    return {
        "status": "ok",
        "env": settings.APP_ENV
    }