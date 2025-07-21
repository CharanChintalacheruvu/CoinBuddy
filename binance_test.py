from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

client = Client(api_key, api_secret)

def test_binance_api():
    try:
        price = client.get_symbol_ticker(symbol="BTCUSDT")
        print("✅ Binance API Connected.")
        print(f"Current BTC Price: ${price['price']}")
    except Exception as e:
        print("❌ Binance API Error:", e)

if __name__ == "__main__":
    test_binance_api()
