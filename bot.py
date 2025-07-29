import os
import logging
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# Load from environment (safe!)
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Fail fast if any key is missing
if not TELEGRAM_TOKEN:
    raise ValueError("TELEGRAM_TOKEN is missing from environment variables!")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is missing from environment variables!")

# Set OpenAI key
openai.api_key = OPENAI_API_KEY

# Logging
logging.basicConfig(level=logging.INFO)

# Bot logic
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    chat_id = update.effective_chat.id

    try:
        # Call ChatGPT
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}],
        )
        reply = response.choices[0].message.content.strip()
    except Exception as e:
        logging.error(f"OpenAI error: {e}")
        reply = "Sorry, something went wrong while contacting OpenAI."

    await context.bot.send_message(chat_id=chat_id, text=reply)

# Entry point
if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
