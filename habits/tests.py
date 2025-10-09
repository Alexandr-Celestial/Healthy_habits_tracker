from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from habits.models import Habit
from users.models import User


class HabitAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email="test@example.com", password="testpass123"
        )
        self.client.login(email="test@example.com", password="testpass123")
        self.client.force_authenticate(user=self.user)
        self.habit_data = {
            "place": "Дома",
            "time": "08:00:00",
            "action": "Утренняя зарядка",
            "is_pleasant": False,
            "periodicity": 1,
            "reward": "",
            "time_to_complete": 2,
            "is_public": True,
        }

    def test_create_habit(self):
        url = reverse("habits:habit_create")
        response = self.client.post(url, self.habit_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 1)
        self.assertEqual(Habit.objects.get().action, "Утренняя зарядка")

    def test_get_habits_list(self):
        Habit.objects.create(user=self.user, **self.habit_data)
        url = reverse("habits:habit_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_update_habit(self):
        habit = Habit.objects.create(user=self.user, **self.habit_data)
        url = reverse("habits:habit_update", args=[habit.id])
        updated_data = {**self.habit_data, "action": "Вечерняя прогулка"}
        response = self.client.put(url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        habit.refresh_from_db()
        self.assertEqual(habit.action, "Вечерняя прогулка")

    def test_delete_habit(self):
        habit = Habit.objects.create(user=self.user, **self.habit_data)
        url = reverse("habits:habit_delete", args=[habit.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.count(), 0)
