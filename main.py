from flask import Flask, request
from telegram import Bot, Update
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/' + TOKEN, methods=['POST'])
def respond():
    update = Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    message = update.message.text

    bot.send_message(chat_id=chat_id, text=f"You said: {message}")
    return 'ok'

@app.route('/')
def index():
    return 'Bot is running.'
