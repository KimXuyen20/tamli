# Generated by Django 5.1.2 on 2024-10-29 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
