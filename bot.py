import os
import openai
from flask import Flask, request
from telegram import Bot, Update

# Load environment variables
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Validate token before creating bot
if not TELEGRAM_TOKEN:
    raise ValueError("TELEGRAM_TOKEN is missing from environment variables!")

bot = Bot(token=TELEGRAM_TOKEN)
openai.api_key = OPENAI_API_KEY

app = Flask(__name__)

# Function to call ChatGPT
def ask_chatgpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # use "gpt-4" if you have access
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"OpenAI error: {e}")
        return "Sorry, I couldn't get an answer."

@app.route(f"/{TELEGRAM_TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)

    if update.message and update.message.text:
        user_input = update.message.text
        chat_id = update.message.chat.id
        reply = ask_chatgpt(user_input)
        bot.send_message(chat_id=chat_id, text=reply)

    return "ok"

@app.route("/", methods=["GET"])
def home():
    return "Bot is live and running!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
