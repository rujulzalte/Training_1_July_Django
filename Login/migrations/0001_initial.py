# Generated by Django 5.0.5 on 2024-07-03 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("username", models.CharField(max_length=25)),
                ("email", models.EmailField(max_length=50)),
                ("date", models.DateField(auto_now_add=True)),
                ("zipcode", models.IntegerField(max_length=10)),
                ("phone", models.IntegerField(max_length=15)),
            ],
        ),
    ]