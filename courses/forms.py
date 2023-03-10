from django.forms import forms

from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["name", "code"]

    def save(self, user=None):
        course = super().save()
        course.lecturers.add(user)
        course.save()
        return course
