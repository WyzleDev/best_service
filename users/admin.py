from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['id', 'username', 'email']
    # create user fields
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'avatar',
                    'first_name',
                    'last_name',
                    'course',
                    'birth_date',
                    'groups',
                )
            }
        )
    )
    # Edit user fields
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'avatar',
                    'course',
                    'birth_date',
                )
            }
        )
    )
