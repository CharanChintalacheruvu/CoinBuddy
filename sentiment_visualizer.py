import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import time
from alerts import play_alert_sound
from ai_optimizer import predict_with_ai

from reddit_sentiment import fetch_reddit_sentiment
from indicators import get_latest_indicators
from decision_engine import make_trade_decision

# Store timestamps and scores
timestamps = []
sentiment_scores = []
rsi_values = []
macd_values = []
decisions = []

def update_chart():
    plt.clf()
    plt.title(f"Live Sentiment + Indicators | Last: {decisions[-1]}")
    plt.xlabel("Time")
    plt.ylabel("Sentiment Score (-1 to +1)")

    plt.gcf().autofmt_xdate()
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))

    # Plot sentiment line
    plt.plot(timestamps, sentiment_scores, marker='o', color='blue', label='Sentiment')

    # Plot RSI & MACD as separate info
    for i, time_point in enumerate(timestamps):
        plt.text(time_point, sentiment_scores[i] + 0.05,
                 f"RSI:{rsi_values[i]:.1f} MACD:{macd_values[i]:.3f}\n{decisions[i]}",
                 fontsize=8, ha='center')

    plt.axhline(0, color='gray', linestyle='--')
    plt.legend()
    plt.pause(0.1)

def run_visualizer(interval=30, duration=300):
    print("📊 Starting Trading Companion Visualizer...")
    plt.ion()

    start_time = time.time()
    while time.time() - start_time < duration:
        current_time = datetime.now()
        
        sentiment = fetch_reddit_sentiment()
        indicators = get_latest_indicators()
        rsi = indicators["rsi"]
        macd = indicators["macd"]
        decision, reason = make_trade_decision(indicators,sentiment)
        ai_decision = predict_with_ai(rsi, macd, sentiment, indicators['bb_upper'], indicators['bb_lower'], indicators['price'])
        print(f"🤖 AI Signal Suggests: {ai_decision}")
        play_alert_sound(decision)


        timestamps.append(current_time)
        sentiment_scores.append(sentiment)
        rsi_values.append(rsi)
        macd_values.append(macd)
        decisions.append(decision)

        print(f"[{current_time.strftime('%H:%M:%S')}] Sentiment: {sentiment:.3f} | RSI: {rsi:.2f} | MACD: {macd:.3f} => 🚦 {decision} ({reason})")

        update_chart()
        time.sleep(interval)

    print("⏹️ Visualization complete.")
    plt.ioff()
    plt.show()

if __name__ == "__main__":
    run_visualizer(interval=30, duration=180)  # Run for 3 mins
