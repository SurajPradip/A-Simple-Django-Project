# Generated by Django 4.2.3 on 2023-07-26 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("register", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="loggers",
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
                ("username", models.CharField(max_length=200)),
                ("method", models.CharField(max_length=200)),
                ("url_path", models.CharField(max_length=200)),
                ("auth", models.BooleanField(blank=True, null=True)),
            ],
        ),
    ]