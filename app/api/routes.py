from fastapi import APIRouter, HTTPException
from app.ingestion.fetcher import fetch_data, tracked_assets, data_store
from app.processing.metrics import calculate_metrics, compare_assets
from app.genai.summarizer import generate_summary
from app.models.schemas import AssetMetrics
from datetime import datetime, timedelta
import pandas as pd
import os

router = APIRouter()


@router.get("/assets")
def get_assets():
    return tracked_assets


@router.post("/ingest")
def ingest():
    try:
        data = fetch_data()
        return {"status": "Data ingested", "data": str(data)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/metrics/{symbol}", response_model=AssetMetrics)
def get_metrics(symbol: str):
    try:
        return calculate_metrics(symbol)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/compare")
def compare(asset1: str, asset2: str):
    try:
        return compare_assets(asset1, asset2)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/summary")
def summary():
    try:
        return {"summary": generate_summary()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/test/mock_data")
def inject_mock_data():
    if os.getenv("ENV") != "development":
        raise HTTPException(
            status_code=403, detail="Mocking allowed only in development")

    now = datetime.now()
    hours = pd.date_range(end=now, periods=168, freq="H")
    close_prices = [63215.0 + ((i % 24) - 12) * 50 for i in range(168)]
    df = pd.DataFrame({"Close": close_prices}, index=hours)
    data_store["BTC"] = df
    return {"status": "mock BTC data injected"}
