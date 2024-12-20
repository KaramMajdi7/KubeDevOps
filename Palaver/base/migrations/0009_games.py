# Generated by Django 4.1.7 on 2023-04-11 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0008_notification_fromuser"),
    ]

    operations = [
        migrations.CreateModel(
            name="Games",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True, null=True)),
                ("image", models.ImageField(blank=True, null=True, upload_to="")),
            ],
        ),
    ]
