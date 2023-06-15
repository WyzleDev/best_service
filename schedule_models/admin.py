from django.contrib import admin
from .models import *
from .models_updated import *


from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget

class LessonResources(resources.ModelResource):
    teacher = fields.Field(column_name="teacher", attribute="teacher", widget=ForeignKeyWidget(Teacher, "last_name"))
    class Meta:
        model = Lesson

class LessonAdmin(ImportExportActionModelAdmin):
    resource_class = LessonResources
    list_display = ["name"]
    list_filter = ["teacher"]


class DayScheduleResoutce(resources.ModelResource):
    lessons = fields.Field(column_name="lessons", attribute="lessons", widget=ManyToManyWidget(Lesson, "\n", "name"))
    group = fields.Field(column_name="group", attribute="group", widget=ForeignKeyWidget(StudentGroup, "name"))
    class Meta:
        model = DaySchedule

class DayScheduleAdmin(ImportExportActionModelAdmin):
    resource_class = DayScheduleResoutce
    list_display = ["date", 'day_of_week', 'group', 'id']
    list_per_page = 7
    list_filter = ['group', 'day_of_week']

class CurrentWeekResource(resources.ModelResource):
    days = fields.Field(column_name="days", attribute="days", widget=ManyToManyWidget(DaySchedule, "day_of_week"))
    group = fields.Field(column_name="group", attribute="group", widget=ForeignKeyWidget(StudentGroup, "name"))
    class Meta:
        model = CurrentWeek

class CurrentWeekScheduleAdmin(ImportExportActionModelAdmin):
    resource_class = CurrentWeekResource
    list_display = ['week_number', 'group']
    list_filter = ['group']


class PreviousWeekScheduleAdmin(admin.ModelAdmin):
    list_display = ['week_number', 'group']
    list_filter = ['group']

class NextWeekScheduleAdmin(admin.ModelAdmin):
    list_display = ['week_number', 'group']
    list_filter = ['group']

    class Meta:
        model = NextWeek
        verbose_name = "Следующая неделя"
        verbose_name_plural = "Следующие недели"

admin.site.register(Teacher)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(DaySchedule, DayScheduleAdmin)
admin.site.register(CurrentWeek, CurrentWeekScheduleAdmin)
admin.site.register(PreviousWeek, PreviousWeekScheduleAdmin)
admin.site.register(NextWeek, NextWeekScheduleAdmin)
