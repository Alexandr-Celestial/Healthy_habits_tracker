from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from bot.serializers import TelegramChatIDSerializer


class TelegramChatIDUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = TelegramChatIDSerializer(data=request.data)
        if serializer.is_valid():
            telegram_id = serializer.validated_data['telegram_id']
            profile = request.user.profile
            profile.telegram_id = telegram_id
            profile.save()
            return Response({'detail': 'Telegram ID сохранён.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
