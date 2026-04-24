import requests
import json
import time

# Константы
API_URL = "http://localhost:8000/ask"

def get_spam_verdict(sms_text: str) -> str:
    """
    Отправляет СМС на FastAPI сервис для классификации
    
    Args:
        sms_text (str): The content of the SMS.
        
    Returns:
        str: '1' for SPAM, '0' for HAM (normal).
    """
    prompt = (
        f"Task: Classify SMS as SPAM or HAM.\n"
        f"Rules: If it's advertising, win, or money request - answer 1.\n"
        f"Answer only with a single digit (0 or 1).\n"
        f"SMS: {sms_text}\n"
        f"Verdict (0/1):"
    )
    
    payload = {"text": prompt}
    
    try:
        response = requests.post(API_URL, json=payload, timeout=30)
        response.raise_for_status()
        raw_output = response.json().get('response', '').strip()
        for char in raw_output:
            if char in "01":
                return char
        return "?"
    except Exception:
        return "Err"

def run_benchmarking():
    """
    Запускает тестирование и выводит таблицу результатов классификации
    """
    test_data = [
        "URGENT! You have won a 1-week HALO ticket. Call 09061701461 to claim.",
        "Hi! Are you coming to the party tonight? Let me know.",
        "FREE entry into our £250 weekly competition. Text WIN to 80082.",
        "I'll be home in 10 minutes. Can you start the kettle?",
        "Your account #1234 has a security alert. Log in at bit.ly/secure-now",
        "Could you please send me the report by EOD? Thanks.",
        "CONGRATULATIONS! You've been selected for a $1000 Walmart gift card!",
        "Don't forget our dental appointment at 4 PM tomorrow.",
        "Get a loan today with 0% interest! No credit check needed. Click here.",
        "Hey, can you call me back when you have a second?"
    ]

    print("="*85)
    print(f"{'SMS SPAM DETECTION SYSTEM PERFORMANCE REPORT (PoC)':^85}")
    print("="*85)
    print(f"{'№':<3} | {'SMS Message Text':<60} | {'Verdict'}")
    print("-" * 85)

    for i, sms in enumerate(test_data, 1):
        start_time = time.time()
        verdict = get_spam_verdict(sms)
        elapsed = time.time() - start_time
        
        display_text = (sms[:57] + '..') if len(sms) > 57 else sms.ljust(59)
        
        if verdict == "1":
            status = "SPAM (1)"
        elif verdict == "0":
            status = "OK   (0)"
        else:
            status = "UNKNOWN "

        print(f"{i:<3} | {display_text:<60} | {status} [{elapsed:.2f}s]")

    print("-" * 85)
    print(f"Legend: 1 - Spam detected, 0 - Safe message")
    print("="*85)

if __name__ == "__main__":
    run_benchmarking()