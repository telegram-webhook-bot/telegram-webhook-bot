
from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, data=payload)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    message = data.get("value1", "（沒有接收到訊息內容）")
    send_telegram_message(message)
    return "OK", 200

@app.route("/", methods=["GET"])
def index():
    return "Webhook server is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
