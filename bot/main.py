 vava94-codex/следовать-файлу-read-me
"""Entry point for the Telegram bot."""


import os
from telegram.ext import Application, CommandHandler

TOKEN = os.environ.get("BOT_TOKEN")


async def start(update, context):
 vava94-codex/следовать-файлу-read-me
    """Respond to the /start command."""


    await update.message.reply_text("Hello from VPN bot!")


def main() -> None:
Я vava94-codex/следовать-файлу-read-me
    """Run the bot in polling mode."""


    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()


if __name__ == "__main__":
    main()
