import logging
from telegram.ext import ApplicationBuilder, CommandHandler
from handlers.start import start_command
from handlers.info import info_command
from config import BOT_TOKEN, BOT_NAME

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(BOT_NAME)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Register handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("info", info_command))

    logger.info(f"{BOT_NAME} bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
