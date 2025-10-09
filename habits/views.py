from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from habits.models import Habit
from habits.paginators import ListHabitPaginator
from habits.serializers import HabitSerializer
from users.permissions import OwnerOrReadOnlyPerm, OwnerOnlyPerm


class HabitCreateAPIView(generics.CreateAPIView):
    """Создание привычки"""

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Сохраняет привычку текущему пользователю"""
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitListAPIView(generics.ListAPIView):
    """Отображение списка привычек"""

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = ListHabitPaginator

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user).order_by("id")


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Предоставляет доступ только владельцам"""

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, OwnerOrReadOnlyPerm]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitUpdateAPUView(generics.UpdateAPIView):
    """Позволяет обновлять привычки только владельцам"""

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, OwnerOnlyPerm]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitDestroyAPIView(generics.DestroyAPIView):
    """Позволяет удалять привычки только владельцам"""

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, OwnerOnlyPerm]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class PublicHabitListAPIView(generics.ListAPIView):
    """Позволяет всем пользователям смотреть список публичных привычек"""

    serializer_class = HabitSerializer
    permission_classes = [AllowAny]
    pagination_class = ListHabitPaginator
    queryset = Habit.objects.filter(is_public=True).order_by("id")
