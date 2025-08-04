from telegram import Update
from telegram.ext import ContextTypes
from config import BOT_NAME

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"👋 Hello {user.first_name}! I am {BOT_NAME}, your assistant.\nType /info to know more."
    )
