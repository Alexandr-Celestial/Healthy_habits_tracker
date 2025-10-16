import telegram
from django.conf import settings

bot = telegram.Bot(token=settings.TELEGRAM_BOT_TOKEN)


def send_telegram_message(chat_id: str, text: str) -> bool:
    """Отправляет сообщения пользователю по chat_id"""

    try:
        bot.send_message(chat_id=chat_id, text=text)
        return True
    except telegram.error.TelegramError as e:
        print(f"Возникла ошибка при отправке сообщения: {e}")
        return False
