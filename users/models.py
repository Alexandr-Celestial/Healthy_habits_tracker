from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CASCADE


class User(AbstractUser):
    """Модель пользователя"""

    username = None

    email = models.EmailField(unique=True, null=False, verbose_name='email', help_text='Введите адрес эл.почты')
    avatar = models.ImageField(upload_to='avatar/', verbose_name='аватар', null=True, blank=True)
    phone_number = models.CharField(max_length=30, verbose_name='номер телефона', null=True, blank=True)
    city = models.CharField(max_length=100, verbose_name='город', null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class UserProfile(models.Model):
    """Модель профиля пользователя"""

    user: User = models.OneToOneField (User, verbose_name="Пользователь", on_delete=CASCADE, null=True, blank=True,
                                related_name="profile")
    telegram_id = models.CharField(max_length=50, blank=True, null=True, unique=True)

    def __str__(self):
        return f"Профиль {self.user.email}"

    class Meta:
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользователя"
