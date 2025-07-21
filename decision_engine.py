def make_trade_decision(indicators, sentiment_score):
    price = indicators['price']
    rsi = indicators['rsi']
    macd = indicators['macd']
    macd_signal = indicators['macd_signal']
    bb_upper = indicators['bb_upper']
    bb_lower = indicators['bb_lower']

    decision = "HOLD"

    # --- RSI logic ---
    if rsi > 70:
        rsi_decision = "SELL"
    elif rsi < 30:
        rsi_decision = "BUY"
    else:
        rsi_decision = "HOLD"

    # --- MACD logic ---
    if macd > macd_signal:
        macd_decision = "BUY"
    elif macd < macd_signal:
        macd_decision = "SELL"
    else:
        macd_decision = "HOLD"

    # --- Bollinger Bands logic ---
    if price >= bb_upper:
        bb_decision = "SELL"
    elif price <= bb_lower:
        bb_decision = "BUY"
    else:
        bb_decision = "HOLD"

    # --- Sentiment logic ---
    if sentiment_score > 0.2:
        sentiment_decision = "BUY"
    elif sentiment_score < -0.2:
        sentiment_decision = "SELL"
    else:
        sentiment_decision = "HOLD"

    # --- Scoring System ---
    scores = {"BUY": 0, "SELL": 0, "HOLD": 0}
    for d in [rsi_decision, macd_decision, bb_decision, sentiment_decision]:
        scores[d] += 1

    # Pick the action with the highest votes
    decision = max(scores, key=scores.get)

    return decision, {
        "rsi": rsi_decision,
        "macd": macd_decision,
        "bb": bb_decision,
        "sentiment": sentiment_decision
    }
