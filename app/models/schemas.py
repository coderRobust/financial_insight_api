from pydantic import BaseModel


class AssetMetrics(BaseModel):
    symbol: str
    latest_price: float
    change_percent_24h: float
    average_price_7d: float
