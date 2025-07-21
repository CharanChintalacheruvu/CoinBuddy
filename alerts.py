# alerts.py
import platform

def play_alert_sound(decision):
    if decision not in ["BUY", "SELL"]:
        return  # No alert for HOLD

    try:
        system = platform.system()
        if system == "Windows":
            import winsound
            frequency = 1000 if decision == "BUY" else 500
            duration = 500
            winsound.Beep(frequency, duration)
        elif system == "Darwin":  # macOS
            import os
            os.system('say "Buy Signal"' if decision == "BUY" else 'say "Sell Signal"')
        else:  # Linux
            print("\a")  # Basic bell sound
    except Exception as e:
        print(f"Alert error: {e}")
