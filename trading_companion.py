import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import time

from reddit_sentiment import fetch_reddit_sentiment
from technical_indicators import get_latest_indicators

# Track data over time
timestamps = []
prices = []
rsi_values = []
sentiments = []
signals = []

# Strategy: Combine RSI + Reddit Sentiment
def make_decision(rsi, sentiment):
    if rsi < 30 and sentiment > 0.2:
        return "BUY"
    elif rsi > 70 and sentiment < -0.2:
        return "SELL"
    else:
        return "HOLD"

def update_plot():
    plt.clf()
    plt.suptitle("Crypto Trading Companion", fontsize=14)

    # PRICE
    plt.subplot(3, 1, 1)
    plt.plot(timestamps, prices, label="Price", color="orange")
    plt.ylabel("Price (USDT)")
    plt.legend()
    plt.grid(True)

    # RSI
    plt.subplot(3, 1, 2)
    plt.plot(timestamps, rsi_values, label="RSI", color="blue")
    plt.axhline(70, color='red', linestyle='--', linewidth=1)
    plt.axhline(30, color='green', linestyle='--', linewidth=1)
    plt.ylabel("RSI")
    plt.legend()
    plt.grid(True)

    # Sentiment & Signal
    plt.subplot(3, 1, 3)
    plt.plot(timestamps, sentiments, label="Sentiment", color="purple")
    for i, txt in enumerate(signals):
        plt.text(timestamps[i], sentiments[i], txt, fontsize=8, ha='center', va='bottom')
    plt.ylabel("Sentiment")
    plt.xlabel("Time")
    plt.legend()
    plt.grid(True)

    # Format x-axis time
    plt.gcf().autofmt_xdate()
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.pause(0.1)

def run_trading_companion(interval=30, duration=180):
    print("🚀 Starting Trading Companion...\n")
    plt.ion()
    start_time = time.time()

    while time.time() - start_time < duration:
        timestamp = datetime.now()
        sentiment = fetch_reddit_sentiment()
        indicators = get_latest_indicators()

        rsi = indicators["rsi"]
        price = indicators["price"]
        decision = make_decision(rsi, sentiment)

        # Save data
        timestamps.append(timestamp)
        prices.append(price)
        rsi_values.append(rsi)
        sentiments.append(sentiment)
        signals.append(decision)

        # Log to console
        print(f"[{timestamp.strftime('%H:%M:%S')}] Price: {price:.2f} | RSI: {rsi:.2f} | Sentiment: {sentiment:.2f} => {decision}")

        update_plot()
        time.sleep(interval)

    plt.ioff()
    plt.close()  # <- This will close the window automatically
    print("✅ Trading Companion session ended.")


if __name__ == "__main__":
    run_trading_companion()