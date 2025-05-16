from app.ingestion.fetcher import data_store
from app.models.schemas import AssetMetrics


def calculate_metrics(symbol: str) -> AssetMetrics:
    df = data_store.get(symbol)
    if df is None or df.empty:
        raise ValueError("No data available for symbol")

    latest_price = df["Close"].iloc[-1].item()
    change_percent_24h = (
        (df["Close"].iloc[-1].item() - df["Close"].iloc[-24].item()) /
        df["Close"].iloc[-24].item()
    ) * 100
    average_price_7d = df["Close"].mean().item()

    return AssetMetrics(
        symbol=symbol,
        latest_price=round(latest_price, 2),
        change_percent_24h=round(change_percent_24h, 2),
        average_price_7d=round(average_price_7d, 2)
    )


def compare_assets(asset1: str, asset2: str):
    m1 = calculate_metrics(asset1)
    m2 = calculate_metrics(asset2)
    return {"comparison": {asset1: m1.model_dump(), asset2: m2.model_dump()}}
