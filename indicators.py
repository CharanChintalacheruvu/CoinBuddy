import pandas as pd
import ta
from binance.client import Client
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

binance_client = Client(api_key=os.getenv("BINANCE_API_KEY"), api_secret=os.getenv("BINANCE_API_SECRET"))

def get_latest_indicators(symbol="BTCUSDT", interval="1m", limit=50):
    klines = binance_client.get_klines(symbol=symbol, interval=interval, limit=limit)
    df = pd.DataFrame(klines, columns=[
        "timestamp", "open", "high", "low", "close", "volume",
        "close_time", "quote_asset_volume", "number_of_trades",
        "taker_buy_base", "taker_buy_quote", "ignore"
    ])
    
    df["close"] = pd.to_numeric(df["close"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit='ms')

    # Optional: Print the latest candle time for real-time verification
    latest_time = df["timestamp"].iloc[-1]
    print(f"[INFO] Latest Binance Kline Timestamp: {latest_time} (UTC)")

    # RSI
    rsi = ta.momentum.RSIIndicator(close=df["close"]).rsi().iloc[-1]

    # MACD
    macd_indicator = ta.trend.MACD(close=df["close"])
    macd = macd_indicator.macd().iloc[-1]
    signal = macd_indicator.macd_signal().iloc[-1]

    # Bollinger Bands
    bb_indicator = ta.volatility.BollingerBands(close=df["close"])
    upper = bb_indicator.bollinger_hband().iloc[-1]
    lower = bb_indicator.bollinger_lband().iloc[-1]

    latest_price = df["close"].iloc[-1]

    return {
        "price": latest_price,
        "rsi": rsi,
        "macd": macd,
        "macd_signal": signal,
        "bb_upper": upper,
        "bb_lower": lower
    }