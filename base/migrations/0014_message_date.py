# Generated by Django 4.1.7 on 2023-04-19 17:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0013_question_completed_by"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="date",
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
