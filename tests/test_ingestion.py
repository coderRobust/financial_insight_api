from app.ingestion.fetcher import fetch_data, data_store


def test_fetch_data():
    fetch_data()
    assert "BTC-USD" in data_store and not data_store["BTC-USD"].empty
