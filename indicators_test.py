from indicators import get_latest_indicators
from reddit_sentiment import fetch_reddit_sentiment  # your existing function
from decision_engine import make_trade_decision

indicators = get_latest_indicators()
sentiment = fetch_reddit_sentiment("bitcoin")  # gives score like 0.05

decision, reasons = make_trade_decision(indicators, sentiment)
print("💡 Final Decision:", decision)
print("📊 Reason Breakdown:", reasons)
