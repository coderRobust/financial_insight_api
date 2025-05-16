from app.processing.metrics import calculate_metrics
from app.ingestion.fetcher import fetch_data


def test_calculate_metrics():
    fetch_data()
    m = calculate_metrics("BTC-USD")
    assert m.latest_price > 0
