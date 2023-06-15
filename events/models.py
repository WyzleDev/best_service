from django.db import models

from users.models import CustomUser

class EventTag(models.Model):
    name = models.CharField(max_length=32, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"


class Event(models.Model):
    banner = models.ImageField(null=True, blank=True)
    header = models.CharField(max_length=128, null=False, blank=False, verbose_name='Название мероприятия')
    event_tags = models.ManyToManyField("EventTag", verbose_name='тэги мероприятия')
    date = models.DateTimeField(verbose_name='Дата и время мероприятия')
    location = models.CharField(max_length=256, verbose_name="Адрес мероприятия")
    participants = models.ManyToManyField(CustomUser, verbose_name='Участники')
    description = models.TextField()
    social_link1 = models.URLField(null=True, blank=True)
    social_link2 = models.URLField(null=True, blank=True)


    def __str__(self):
        return f'{self.header}'

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"
