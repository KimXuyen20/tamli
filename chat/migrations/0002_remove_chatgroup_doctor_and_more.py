# Generated by Django 5.1.2 on 2024-11-01 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatgroup',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='chatgroup',
            name='groupchat_name',
        ),
        migrations.RemoveField(
            model_name='chatgroup',
            name='is_private',
        ),
        migrations.RemoveField(
            model_name='chatgroup',
            name='members',
        ),
        migrations.RemoveField(
            model_name='chatgroup',
            name='users_online',
        ),
    ]