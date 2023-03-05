# Generated by Django 4.1.7 on 2023-03-05 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("assessments", "0001_initial"),
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
                ("student_number", models.CharField(max_length=9, unique=True)),
                ("full_names", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Submission",
            fields=[
                (
                    "id",
                    models.CharField(
                        editable=False, max_length=20, primary_key=True, serialize=False
                    ),
                ),
                ("attachment", models.FileField(upload_to="")),
                ("ip_address", models.GenericIPAddressField()),
                ("submission_times", models.IntegerField(default=1)),
                ("submitted_at", models.DateTimeField(auto_now_add=True)),
                (
                    "assessment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="assessments.assessment",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="submissions.student",
                    ),
                ),
            ],
        ),
    ]
