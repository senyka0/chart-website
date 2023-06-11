import requests
import pandas as pd

symbol = "BTCUSDT"  # your symbol
interval = "1d"  # your interval (1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M)


def collect_data(symbol, interval):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(
            data,
            columns=[
                "Open Time",
                "Open",
                "High",
                "Low",
                "Close",
                "Volume",
                "Close Time",
                "Quote Asset Volume",
                "Number of Trades",
                "Taker Buy Base Asset Volume",
                "Taker Buy Quote Asset Volume",
                "Ignore",
            ],
        )
        
        df["Open Time"] = pd.to_datetime(df["Open Time"], unit="ms")
        df["Close Time"] = pd.to_datetime(df["Close Time"], unit="ms")

        return df
    else:
        return None


data = collect_data(symbol, interval)
filename = f"{symbol}_{interval}.csv"
data.to_csv(filename, index=False)
