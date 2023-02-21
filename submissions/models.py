import uuid

from django.db import models

from assessments.models import Assessment


class Submission(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    submission_time = models.DateTimeField(auto_now_add=True)
    attachment = models.FileField()
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
