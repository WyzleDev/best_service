from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    avatar = models.ImageField(_("avatar"), null=True, blank=True)
    course = models.PositiveIntegerField(_("Курс"), null=True, blank=True)
    birth_date = models.DateField(_("Дата рождения"), null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
