from django.db import models
from groups.models import StudentGroup


class Teacher(models.Model):
    avatar = models.ImageField(null=True, blank=True, upload_to='media/')
    first_name = models.CharField(max_length=64, null=False, blank=False)
    last_name = models.CharField(max_length=64, null=False, blank=False)
    bio = models.TextField(blank=True, null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"


class Lesson(models.Model):
    avatar = models.ImageField(upload_to='media/', null=True)
    name = models.CharField(max_length=32, blank=False, null=False)
    teacher = models.ManyToManyField(Teacher, verbose_name='Учителя')
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class DaySchedule(models.Model):
    date = models.CharField(max_length=32, blank=False, null=False)
    day_of_week = models.CharField(max_length=32, blank=True, null=True)
    group = models.ForeignKey(StudentGroup, on_delete=models.DO_NOTHING, null=False, blank=False)
    lessons = models.ManyToManyField("Lesson", related_name="lesson_day")

    def __str__(self) -> str:
        return f"{self.day_of_week} | {self.date}"

    class Meta:
        verbose_name = "дневное расписание"
        verbose_name_plural = "дневные расписания"
