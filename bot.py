from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

import os

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot RevealMeAI actif !")

app = ApplicationBuilder().token(os.environ["BOT_TOKEN"]).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
