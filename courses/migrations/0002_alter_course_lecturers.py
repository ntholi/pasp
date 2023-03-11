# Generated by Django 4.1.7 on 2023-03-10 07:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("courses", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="lecturers",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]