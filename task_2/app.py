from flask import Flask, render_template
import plotly.graph_objs as go
import pandas as pd
import requests

symbol = "BTCUSDT"  # your symbol
interval = "1d"  # your interval (1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M)

app = Flask(__name__)


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


def get_market_caps():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        symbols = [coin["symbol"] for coin in data]
        market_caps = [coin["market_cap"] for coin in data]
        return symbols, market_caps
    else:
        return None


@app.route("/")
def index():
    df = collect_data(symbol, interval)
    candlestick = go.Candlestick(
        x=df["Open Time"],
        open=df["Open"],
        high=df["High"],
        low=df["Low"],
        close=df["Close"],
    )
    symbols, market_caps = get_market_caps()
    piechart = go.Pie(labels=symbols, values=market_caps)
    layout = go.Layout(
        title="Candlestick Chart", xaxis=dict(title="Date"), yaxis=dict(title="Price")
    )
    chart_data = go.Figure(data=candlestick, layout=layout).to_json()
    pie_data = go.Figure(data=piechart).to_json()

    return render_template("index.html", chart_data=chart_data, pie_data=pie_data)


if __name__ == "__main__":
    app.run(debug=True)
