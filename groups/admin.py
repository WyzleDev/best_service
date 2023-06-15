from django.contrib import admin

from users.models import CustomUser
from .models import StudentGroup
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget


class StudentGroupResources(resources.ModelResource):
    students = fields.Field(column_name="students", attribute="students", widget=ManyToManyWidget(CustomUser, ",", "username"))
    class Meta:
        model = StudentGroup
        exclude = ("group_ptr", 'permissions')
@admin.register(StudentGroup)
class StudentGroupAdmin(GroupAdmin, ImportExportActionModelAdmin):
    resource_class = StudentGroupResources
    list_display = ["name", "course"]


admin.site.unregister(Group)
