import tkinter as tk
from tkinter import ttk
from reddit_sentiment import fetch_reddit_sentiment
from indicators import get_latest_indicators
from decision_engine import make_trade_decision

def refresh_data():
    sentiment = fetch_reddit_sentiment()
    indicators = get_latest_indicators()
    decision, reasons = make_trade_decision(indicators, sentiment)

    sentiment_label.config(text=f"Sentiment Score: {sentiment:.3f}")
    price_label.config(text=f"Price: ${indicators['price']:.2f}")
    rsi_label.config(text=f"RSI: {indicators['rsi']:.2f}")
    macd_label.config(text=f"MACD: {indicators['macd']:.4f} (Signal: {indicators['macd_signal']:.4f})")
    bb_label.config(text=f"Bollinger Bands: Upper={indicators['bb_upper']:.2f}, Lower={indicators['bb_lower']:.2f}")
    decision_label.config(text=f"Trade Decision: {decision}")
    reasons_label.config(text=f"Reasons: {reasons}")

# GUI setup
root = tk.Tk()
root.title("Crypto Trading Companion Dashboard")
root.geometry("500x400")

style = ttk.Style()
style.configure("TLabel", font=("Segoe UI", 11))
style.configure("TButton", font=("Segoe UI", 11, "bold"))

ttk.Label(root, text="Crypto Trading Companion", font=("Segoe UI", 16, "bold")).pack(pady=10)

sentiment_label = ttk.Label(root, text="Sentiment Score:")
price_label = ttk.Label(root, text="Price:")
rsi_label = ttk.Label(root, text="RSI:")
macd_label = ttk.Label(root, text="MACD:")
bb_label = ttk.Label(root, text="Bollinger Bands:")
decision_label = ttk.Label(root, text="Trade Decision:")
reasons_label = ttk.Label(root, text="Reasons:")

for widget in [sentiment_label, price_label, rsi_label, macd_label, bb_label, decision_label, reasons_label]:
    widget.pack(pady=5)

ttk.Button(root, text="🔄 Refresh Data", command=refresh_data).pack(pady=15)

ttk.Label(root, text="© 2025 Charan Sai | All Rights Reserved", font=("Segoe UI", 9), foreground="gray").pack(pady=(20, 5))

# First load
refresh_data()
root.mainloop()
