# Generated by Django 4.0.4 on 2022-05-27 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_todo_is_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='is_updated',
        ),
    ]