import os
from telegram.ext import Application, CommandHandler

TOKEN = os.environ.get("BOT_TOKEN")


async def start(update, context):
    await update.message.reply_text("Hello from VPN bot!")


def main() -> None:
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()


if __name__ == "__main__":
    main()
