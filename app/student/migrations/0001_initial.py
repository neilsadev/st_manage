# Generated by Django 4.1.1 on 2022-10-05 18:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("institute", "0003_alter_department_options_alter_institute_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("first_name", models.CharField(max_length=200)),
                ("last_name", models.CharField(max_length=200)),
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=50)),
                ("birthyear", models.IntegerField()),
                ("address", models.CharField(max_length=500)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="students",
                        to="institute.department",
                    ),
                ),
            ],
        ),
    ]
