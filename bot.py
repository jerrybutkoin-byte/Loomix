import os
from telegram.ext import Application, MessageHandler, filters

BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def echo(update, context):
    await update.message.reply_text("Привет! Я работаю!")

def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(MessageHandler(filters.TEXT, echo))
    print("Bot started!")
    application.run_polling()

if __name__ == "__main__":
    main()
