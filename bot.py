import os
import telegram
from telegram.ext import Updater, MessageHandler, Filters

BOT_TOKEN = os.environ.get("BOT_TOKEN")

def echo(update, context):
    update.message.reply_text("Привет! Я работаю!")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, echo))
    print("Bot started!")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
