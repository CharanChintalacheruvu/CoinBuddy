# ai_optimizer.py
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

model_path = "ai_model.pkl"

# Step 1: Simulate Training (You can later replace this with real data)
def generate_dummy_training_data():
    X = []
    y = []

    for _ in range(500):
        rsi = np.random.uniform(10, 90)
        macd = np.random.uniform(-5, 5)
        sentiment = np.random.uniform(-1, 1)
        bb_distance = np.random.uniform(-300, 300)

        features = [rsi, macd, sentiment, bb_distance]

        if rsi < 30 and sentiment > 0.2 and macd > 0:
            label = 1  # BUY
        elif rsi > 70 and sentiment < -0.2 and macd < 0:
            label = -1  # SELL
        else:
            label = 0  # HOLD

        X.append(features)
        y.append(label)

    return np.array(X), np.array(y)

# Step 2: Train the model (one-time)
def train_model():
    X, y = generate_dummy_training_data()
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)
    joblib.dump(model, model_path)
    print("✅ AI model trained and saved.")

# Step 3: Predict using model
def predict_with_ai(rsi, macd, sentiment, bb_upper, bb_lower, price):
    if not os.path.exists(model_path):
        train_model()

    model = joblib.load(model_path)
    bb_distance = price - ((bb_upper + bb_lower) / 2)
    features = np.array([[rsi, macd, sentiment, bb_distance]])
    prediction = model.predict(features)[0]

    return {1: "BUY", -1: "SELL", 0: "HOLD"}[prediction]