from django.db import models
from django.contrib.auth.models import Group

from users.models import CustomUser


class StudentGroupManager(models.Manager):
    def get_query_set(self):
        return super(StudentGroupManager, self).get_query_set().filter(student__enrolled=True).distinct()


class StudentGroup(Group):
    course = models.IntegerField()
    students = models.ManyToManyField(CustomUser, related_name="student_group", blank=True)

    objects = models.Manager()
    has_students = StudentGroupManager()

    class Meta:
        verbose_name_plural = "Groups"
        ordering = ['name']

    def __unicode__(self):
        return self.name
