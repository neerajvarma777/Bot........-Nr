from telegram import Update
from telegram.ext import ContextTypes
from config import BOT_NAME, DEVELOPER

async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🤖 {BOT_NAME}\nDeveloped by: {DEVELOPER}\nPowered by Python and Telegram API."
    )
