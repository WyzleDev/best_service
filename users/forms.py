from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'avatar', 'course', 'birth_date', 'groups')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'avatar', 'course', 'birth_date', 'groups')
