# 🧠 Crypto Trading Companion

A real-time, intelligent crypto trading assistant that uses **Reddit sentiment analysis** and **Binance technical indicators** to help you make smarter BUY/SELL/HOLD decisions.

## 🚀 Features

- ✅ Live sentiment analysis from Reddit
- ✅ Real-time market data from Binance
- ✅ Key technical indicators: RSI, MACD, Bollinger Bands
- ✅ AI-powered trade decision engine
- ✅ Interactive visualization (Matplotlib)
- ✅ GUI Dashboard (Tkinter)
- ✅ Logging & monitoring
- ✅ Easily extensible and production-ready

---

## 🧰 Technologies Used

- Python 3.10+
- PRAW (Python Reddit API Wrapper)
- Binance API (via `python-binance`)
- `pandas`, `ta` (Technical Analysis Library)
- `matplotlib`, `tkinter`
- `dotenv` for secure credential management

---

## 📊 How It Works

1. **Reddit Sentiment Analysis:**  
   Scans top crypto subreddits and extracts sentiment score based on post titles using the VADER sentiment engine.

2. **Market Indicators:**  
   Pulls live market data from Binance for BTC/USDT and calculates:
   - RSI (Relative Strength Index)
   - MACD (Moving Average Convergence Divergence)
   - Bollinger Bands

3. **Decision Engine:**  
   Combines sentiment and indicator values to suggest a real-time trade decision (BUY / SELL / HOLD).

4. **Visualizer + Dashboard:**  
   - Live console and chart visualizer (CLI)
   - Optional desktop dashboard using Tkinter

---

## 🖥️ How to Run

1. **Install dependencies**
   ```bash
 #  pip install -r requirements.txt
