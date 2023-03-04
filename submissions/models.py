import os.path
from django.db import models
from assessments.models import Assessment


class Student(models.Model):
    student_number = models.CharField(
        max_length=9, unique=True, blank=False, null=False
    )
    full_names = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.full_names} ({self.student_number})"


class Submission(models.Model):
    id = models.CharField(max_length=20, primary_key=True, editable=False)
    attachment = models.FileField()
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    submission_times = models.IntegerField(default=1)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        student_number = self.student.student_number
        file_extension = self.attachment.name.split(".")[-1]
        file_name = f"{student_number}.{file_extension}"
        self.attachment.name = os.path.join(self.assessment.upload_folder, file_name)
        self.id = f"{self.assessment_id}_{student_number}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Submission for ({self.assessment.title})"
