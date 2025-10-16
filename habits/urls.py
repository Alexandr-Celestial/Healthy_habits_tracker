from django.urls import path
from rest_framework.routers import DefaultRouter

from habits.apps import HabitsConfig
from habits.views import (
    HabitListAPIView,
    HabitCreateAPIView,
    HabitRetrieveAPIView,
    HabitUpdateAPUView,
    HabitDestroyAPIView,
    PublicHabitListAPIView,
)

app_name = HabitsConfig.name

router = DefaultRouter()

urlpatterns = [
    path("habit/", HabitListAPIView.as_view(), name="habit_list"),
    path("habit_create/", HabitCreateAPIView.as_view(), name="habit_create"),
    path("habit/<int:pk>/", HabitRetrieveAPIView.as_view(), name="habit_get"),
    path("habit/update/<int:pk>/", HabitUpdateAPUView.as_view(), name="habit_update"),
    path("habit/delete/<int:pk>/", HabitDestroyAPIView.as_view(), name="habit_delete"),
    path("public/", PublicHabitListAPIView.as_view(), name="public_list"),
] + router.urls
