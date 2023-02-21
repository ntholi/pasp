# Generated by Django 4.1.7 on 2023-02-21 14:03

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("assessments", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Submission",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("submission_time", models.DateTimeField(auto_now_add=True)),
                ("attachment", models.FileField(upload_to="")),
                (
                    "assessment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="assessments.assessment",
                    ),
                ),
            ],
        ),
    ]