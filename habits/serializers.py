from rest_framework import serializers

from habits.models import Habit
from habits.validators import validate_habit_fields


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Habit"""

    class Meta:
        model = Habit
        fields = "__all__"

    def validate_habit(self, data):
        """Обработка валидатором"""

        habit = Habit(**data)
        validate_habit_fields(habit)
        return data

