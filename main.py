import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import asyncio

app = Flask(__name__)

TOKEN = os.getenv("BOT_TOKEN")

# ---------------- TELEGRAM BOT ----------------

application = Application.builder().token(TOKEN).build()

# simple /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is running ✅")

application.add_handler(CommandHandler("start", start))

# ---------------- WEBHOOK ROUTE ----------------

@app.route("/")
def home():
    return "Bot is running"

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(force=True)

    update = Update.de_json(data, application.bot)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(application.process_update(update))

    return "ok"

# ---------------- START SERVER ----------------

def run():
    print("Bot starting...")

    # webhook set automatically
    if os.getenv("RENDER_EXTERNAL_URL"):
        url = os.getenv("RENDER_EXTERNAL_URL") + "/webhook"
        print("Webhook mode:", url)

    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    run()
