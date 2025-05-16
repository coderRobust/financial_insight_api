import yfinance as yf
from datetime import datetime, timedelta

tracked_assets = ["BTC-USD", "ETH-USD", "TSLA"]
data_store = {}


def fetch_data():
    global data_store
    end = datetime.now()
    start = end - timedelta(days=7)

    for symbol in tracked_assets:
        df = yf.download(symbol, start=start, end=end, interval="1h")
        print(f"\n=== {symbol} ===")
        if df.empty:
            print(f"No data found for {symbol}")
        else:
            data_store[symbol] = df
            print(df.head())  # Show top few rows for sanity

    return data_store
