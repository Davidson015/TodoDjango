# Generated by Django 4.0.4 on 2022-05-27 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_todo_is_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='is_updated',
            field=models.BooleanField(default=False),
        ),
    ]
