import pandas as pd
from binance.client import Client
from dotenv import load_dotenv
import os
import ta

# 1. Load Binance API Keys
load_dotenv()
client = Client(
    api_key=os.getenv("xAB2L5cpEGir3NiOpu50aCfjA9Ybv9UC4HJ9zn7BSyzVerXbeBwWFEUui6zmplYm"),
    api_secret=os.getenv("QmhpY1EUNgeqMCmWJWJocObypT9LRmusdRd9jLSCvpzWKXPxaMdoE2rqnKQ7k1CI")
)

# 2. Get candlestick data from Binance
def get_ohlcv(symbol="BTCUSDT", interval=Client.KLINE_INTERVAL_1HOUR, limit=100):
    klines = client.get_klines(symbol=symbol, interval=interval, limit=limit)

    df = pd.DataFrame(klines, columns=[
        "timestamp", "open", "high", "low", "close", "volume",
        "close_time", "quote_asset_volume", "num_trades",
        "taker_buy_base", "taker_buy_quote", "ignore"
    ])

    # Convert values to floats for math
    df["close"] = df["close"].astype(float)
    df["open"] = df["open"].astype(float)
    df["high"] = df["high"].astype(float)
    df["low"] = df["low"].astype(float)
    df["volume"] = df["volume"].astype(float)
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    return df

# 3. Add RSI, MACD, and EMA indicators
def calculate_indicators(df):
    df["rsi"] = ta.momentum.RSIIndicator(df["close"], window=14).rsi()
    macd = ta.trend.MACD(df["close"])
    df["macd"] = macd.macd()
    df["macd_signal"] = macd.macd_signal()
    df["ema_20"] = ta.trend.EMAIndicator(df["close"], window=20).ema_indicator()
    return df

# 4. Get latest values (last row)
def get_latest_indicators(symbol="BTCUSDT"):
    df = get_ohlcv(symbol)
    df = calculate_indicators(df)
    latest = df.iloc[-1]
    return {
        "price": latest["close"],
        "rsi": latest["rsi"],
        "macd": latest["macd"],
        "macd_signal": latest["macd_signal"],
        "ema_20": latest["ema_20"]
    }
