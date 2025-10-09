from django.urls import path

from bot.apps import BotConfig
from bot.views import TelegramChatIDUpdateAPIView

app_name = BotConfig.name

urlpatterns = [
    path(
        "telegram-chat-id/",
        TelegramChatIDUpdateAPIView.as_view(),
        name="telegram_chat_id_update",
    ),
]
