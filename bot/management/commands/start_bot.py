import os

from django.core.management import BaseCommand
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, ApplicationBuilder

from dotenv import load_dotenv

load_dotenv()

TG_TOKEN = os.getenv("TG_TOKEN")

class Command(BaseCommand):
    help = "Запускает Телеграм-бота"

    def handle(self, *args, **options):

        async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
            await update.message.reply_text('Привет! Я ваш бот привычек')

        app = ApplicationBuilder().token(TG_TOKEN).build()

        app.add_handler(CommandHandler("start", start))

        app.run_polling()