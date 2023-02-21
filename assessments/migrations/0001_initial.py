# Generated by Django 4.1.7 on 2023-02-21 12:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Assessment",
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
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False)),
                ("title", models.CharField(max_length=100)),
                ("lecturer", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                ("course_name", models.CharField(max_length=100)),
                ("course_code", models.CharField(blank=True, max_length=20)),
                (
                    "question_paper",
                    models.FileField(blank=True, upload_to="question_papers/"),
                ),
                ("start_time", models.DateTimeField()),
                ("end_time", models.DateTimeField()),
                ("cover_image", models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]