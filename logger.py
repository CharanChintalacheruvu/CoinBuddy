# logger.py

import csv
import os
from datetime import datetime

LOG_FILE = "trade_log.csv"

def init_log():
    """Create file with headers if it doesn't exist."""
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, mode="w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                "timestamp", "price", "sentiment", "rsi", "macd", "macd_signal",
                "bb_upper", "bb_lower", "decision", "rsi_decision",
                "macd_decision", "bb_decision", "sentiment_decision"
            ])

def log_snapshot(indicators, sentiment, decision, reasons):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, mode="a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            timestamp,
            indicators["price"],
            sentiment,
            indicators["rsi"],
            indicators["macd"],
            indicators["macd_signal"],
            indicators["bb_upper"],
            indicators["bb_lower"],
            decision,
            reasons["rsi"],
            reasons["macd"],
            reasons["bb"],
            reasons["sentiment"]
        ])
