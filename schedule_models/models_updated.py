from django.db import models
from .models import Lesson, StudentGroup, DaySchedule




class PreviousWeek(models.Model):
    week_number = models.SmallIntegerField()
    days = models.ManyToManyField(DaySchedule)
    group = models.ForeignKey(StudentGroup, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "предыдущую неделю"
        verbose_name_plural = "предыдущие недели"

    def __str__(self):
        return f'{self.week_number}'


class CurrentWeek(models.Model):
    week_number = models.SmallIntegerField()
    days = models.ManyToManyField(DaySchedule)
    group = models.ForeignKey(StudentGroup, on_delete=models.DO_NOTHING, null=True)

    class Meta:
        verbose_name = "текущая неделя"
        verbose_name_plural = "текущие недели"

    def __str__(self):
        return f'{self.week_number}'


class NextWeek(models.Model):
    week_number = models.SmallIntegerField()
    days = models.ManyToManyField(DaySchedule)
    group = models.CharField(max_length=128, null=True)

    class Meta:
        verbose_name = "следующую неделю"
        verbose_name_plural = "следующие недели"

    def __str__(self):
        return f'{self.week_number}'
