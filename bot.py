import requests
import time

BOT_TOKEN = "8700792697:AAGbcEeJXH7eqCxt3p_arWZBRR8InsQTdw8"
CHANNEL = "@Dream_Life_Official_Help_Centre"

MESSAGE = """
📢 Dream Life Official

স্বাগতম আমাদের অফিসিয়াল চ্যানেলে!

👉 https://t.me/Dream_Life_Official_Help_Centre
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

while True:
    requests.post(url, data={
        "chat_id": CHANNEL,
        "text": MESSAGE
    })
    print("Message sent")
    time.sleep(3600)  # প্রতি ১ ঘণ্টা পর পোস্ট
