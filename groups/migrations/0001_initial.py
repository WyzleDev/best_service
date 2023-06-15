# Generated by Django 4.1.7 on 2023-04-04 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentGroup',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.group')),
                ('course', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Groups',
                'ordering': ['name'],
            },
            bases=('auth.group',),
        ),
    ]
