# Generated by Django 4.1 on 2023-01-03 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recognition', '0005_rename_userid_attendance_username_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='user', max_length=20, unique=True),
        ),
    ]
