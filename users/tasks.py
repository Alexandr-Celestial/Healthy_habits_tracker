from celery import shared_task

from bot.utils import send_telegram_message
from users.models import User, UserProfile


@shared_task
def send_telegram_reminder(user_id, message):
    try:
        user = User.objects.get(id=user_id)
        chat_id = UserProfile.telegram_id
        if chat_id:
            send_telegram_message(chat_id, message)
    except Exception as e:
        print(f"Возникла ошибка: {e}")

@shared_task
def send_daily_reminders():
    users = User.objects.filter(profile__telegram_chat_id__isnull=False)
    message = "Пора выполнить вашу привычку!"
    for user in users:
        send_telegram_reminder.delay(user.id, message)
