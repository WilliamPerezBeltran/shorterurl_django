# Generated by Django 2.2 on 2020-07-08 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Url",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url_text", models.CharField(max_length=200)),
                ("url_base62", models.CharField(max_length=200)),
            ],
        ),
    ]
