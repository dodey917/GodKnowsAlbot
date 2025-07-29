# 🤖 ChatGPT Telegram Bot

A simple Telegram bot powered by OpenAI's ChatGPT (GPT-3.5-turbo), deployed securely using [Render.com](https://render.com).  
**No API keys are exposed** — all secrets are stored as environment variables.

---

## ✨ Features

- Uses OpenAI's GPT-3.5-turbo to reply naturally to user messages
- Built with `python-telegram-bot` (v20+)
- No `.env` or API keys in the code
- Deployable to Render with just a few clicks

---

## 🚀 Live Demo

You can interact with your bot once it's deployed by searching for it on Telegram or via the bot URL:

https://t.me/GodKnowsAlbot

---

## 🧠 Powered By

- [OpenAI GPT](https://platform.openai.com/docs/guides/gpt)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [Render.com](https://render.com) (free web hosting & deployment)

---

## 📁 Project Structure

your-chatgpt-telegram-bot/
├── bot.py # Main bot logic
├── requirements.txt # Python dependencies
├── .env.example # Env variable template (DO NOT add real keys here)
├── .gitignore # Keep secrets out of Git
└── README.md # You're here!

---

## ⚙️ Environment Variables (Set in Render)

Create two environment variables in [Render > Environment](https://dashboard.render.com/):

| Key              | Description                   |
|------------------|-------------------------------|
| `TELEGRAM_TOKEN` | Your bot token from @BotFather |
| `OPENAI_API_KEY` | Your OpenAI API key            |

---

## 🛠️ Deploy to Render

1. Push your code to a GitHub repo
2. Go to [Render Dashboard](https://dashboard.render.com/)
3. Click **"New Web Service"**
4. Connect your GitHub repo
5. Use these settings:

| Option            | Value                            |
|-------------------|----------------------------------|
| Runtime           | Python 3.11 or higher             |
| Build Command     | `pip install -r requirements.txt` |
| Start Command     | `python bot.py`                   |

6. Set the **Environment Variables** listed above
7. Click **Deploy**

---

## 🧪 Local Development (optional)

> 🔐 **Never commit your `.env` file!**

If running locally, copy `.env.example` to `.env` and add your keys:

```bash
cp .env.example .env
