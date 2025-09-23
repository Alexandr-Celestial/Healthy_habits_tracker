from django.core.exceptions import ValidationError


def validate_habit_fields(habit):
    """Валидация привычек"""

    if habit.related_habit and habit.reward:
        raise ValidationError(
            "В модели не должно быть заполнено одновременно и поле вознаграждения, и поле связанной привычки. "
            "Можно заполнить только одно из двух полей.")
    if habit.time_to_complete > 120:
        raise ValidationError("Время выполнения должно быть не больше 120 секунд.")
    if habit.is_pleasant and (habit.reward or habit.related_habit):
        raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки.")
    if not (1 <= habit.periodicity <= 7):
        raise ValidationError("Периодичность должна быть не меньше 1 и не больше 7 дней.")
