import os
import openai
from flask import Flask, request
import telegram

# Load environment variables
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY
bot = telegram.Bot(token=TELEGRAM_TOKEN)

app = Flask(__name__)

def chatgpt_response(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Or "gpt-3.5-turbo"
            messages=[{"role": "user", "content": message}],
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("OpenAI error:", e)
        return "Sorry, something went wrong."

@app.route(f"/{TELEGRAM_TOKEN}", methods=["POST"])
def receive_update():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    user_message = update.message.text

    reply = chatgpt_response(user_message)
    bot.send_message(chat_id=chat_id, text=reply)
    return "ok"

@app.route("/", methods=["GET"])
def home():
    return "Bot is running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
