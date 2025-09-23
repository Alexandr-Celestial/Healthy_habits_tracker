from rest_framework import serializers


class TelegramChatIDSerializer(serializers.Serializer):
    telegram_id = serializers.CharField(max_length=50)