from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls.base import reverse
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    """Модель пользователя """

    username = models.CharField(
        _("Никнейм"), max_length=75, unique=True
    )
    email = models.EmailField(
        _("Электронная почта"), unique=True,
    )
    object = UserManager()
    first_name = models.CharField(
        _("Фамилия"), max_length=25, null=True, blank=True
    )
    last_name = models.CharField(
        _("Имя"), max_length=25, null=True, blank=True
    )
    registration = models.DateTimeField('Регистрация', auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователь'
        ordering = ["-registration"]

    def __str__(self):
        return self.username

    def get_full_name(self) -> str:
        """Получение фамилии и имя пользователя"""

        full_name = f'{self.last_name} {self.first_name}'
        return full_name.strip().title()

    def get_absolute_url(self):
        return reverse('profile', kwargs={'username': self.username})
