from django.db import models
from django.db.models import CASCADE

from habits.validators import validate_habit_fields
from users.models import User


class Habit(models.Model):
    """Модель привычки"""

    user = models.ForeignKey(
        User, verbose_name="Пользователь", on_delete=CASCADE, null=True, blank=True
    )
    place = models.CharField(
        max_length=100, verbose_name="Место", null=True, blank=True
    )
    time = models.TimeField(null=True, blank=True, verbose_name="Время")
    action = models.CharField(
        max_length=100, verbose_name="Действие", null=True, blank=True
    )
    is_pleasant = models.BooleanField(
        default=False, verbose_name="Признак приятной привычки", null=True, blank=True
    )
    related_habit = models.ForeignKey(
        "self",
        verbose_name="Связанная привычка",
        on_delete=CASCADE,
        related_name="linked_habits",
        limit_choices_to={"is_pleasant": True},
        null=True,
        blank=True,
    )
    periodicity = models.PositiveSmallIntegerField(
        default=1, help_text="Периодичность", null=True, blank=True
    )
    reward = models.CharField(
        max_length=250, verbose_name="Вознаграждение", null=True, blank=True
    )
    time_to_complete = models.PositiveSmallIntegerField(
        default=60, help_text="Время выполнения в секундах", null=True, blank=True
    )
    is_public = models.BooleanField(
        default=False, verbose_name="Признак публичности", null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        validate_habit_fields(self)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Я буду {self.action} в {self.time} в {self.place}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
