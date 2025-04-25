from telegram import Update
from flask import Flask, request
import telegram
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/' + TOKEN, methods=['POST'])
def respond():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    message = update.message.text

    bot.sendMessage(chat_id=chat_id, text="Hello! I got your message.")
    return 'ok'

@app.route('/')
def index():
    return 'Bot is running'

@app.route('/setwebhook')
def set_webhook():
    webhook_url = os.getenv("WEBHOOK_URL") + TOKEN
    success = bot.setWebhook(url=webhook_url)
    return 'Webhook set: ' + str(success)

if __name__ == '__main__':
    app.run(debug=True)
