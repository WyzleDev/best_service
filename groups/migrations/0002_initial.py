# Generated by Django 4.1.7 on 2023-04-04 12:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentgroup',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='student_group', to=settings.AUTH_USER_MODEL),
        ),
    ]
