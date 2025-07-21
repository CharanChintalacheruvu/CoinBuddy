# main.py

import time
from sentiment_visualizer import run_visualizer
from reddit_sentiment import fetch_reddit_sentiment
from indicators import get_latest_indicators
from decision_engine import make_trade_decision

def print_latest_snapshot():
    print("\n📈 Pulling latest market + sentiment data...\n")
    sentiment = fetch_reddit_sentiment()
    indicators = get_latest_indicators()
    decision, reasons = make_trade_decision(indicators, sentiment)

    print(f"💬 Sentiment Score: {sentiment:.3f}")
    print(f"📉 Price: ${indicators['price']:.2f}")
    print(f"📊 RSI: {indicators['rsi']:.2f}, MACD: {indicators['macd']:.4f}, Signal: {indicators['macd_signal']:.4f}")
    print(f"📈 Bollinger Bands: Upper={indicators['bb_upper']:.2f}, Lower={indicators['bb_lower']:.2f}")
    print(f"\n🚦 Trade Decision: {decision}")
    print(f"🔍 Reason Breakdown: {reasons}\n")

def main():
    print("🧠 Crypto Trading Companion: Initiated")
    print("========================================")

    # Snapshot print of latest state
    print_latest_snapshot()

    # Run live visualizer
    print("📊 Launching live visualizer for next 3 minutes...")
    run_visualizer(interval=30, duration=180)

    print("✅ Session complete.")

if __name__ == "__main__":
    main()
