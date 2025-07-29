import os
import openai
from flask import Flask, request
from telegram import Bot, Update
from telegram.constants import ParseMode
from telegram.helpers import escape_markdown

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY
bot = Bot(token=TELEGRAM_TOKEN)

app = Flask(__name__)

def chatgpt_response(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": message}],
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("OpenAI error:", e)
        return "Sorry, something went wrong."

@app.route(f"/{TELEGRAM_TOKEN}", methods=["POST"])
def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, bot)

    if update.message:
        chat_id = update.message.chat.id
        user_text = update.message.text

        reply = chatgpt_response(user_text)
        bot.send_message(chat_id=chat_id, text=reply, parse_mode=ParseMode.MARKDOWN_V2)

    return "ok"

@app.route("/", methods=["GET"])
def home():
    return "Bot is running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
