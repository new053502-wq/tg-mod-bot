import os
from flask import Flask
from telegram.ext import Application

app = Flask(__name__)

# HEALTH CHECK (Render ke liye zaroori)
@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/")
def home():
    return "Bot is running"

# TELEGRAM BOT START
def run_bot():
    token = os.getenv("BOT_TOKEN")

    if not token:
        print("BOT_TOKEN missing")
        return

    application = Application.builder().token(token).build()

    print("Bot started")
    application.run_polling()

if __name__ == "__main__":
    from threading import Thread

    Thread(target=run_bot).start()

    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
