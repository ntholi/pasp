from django import forms
from submissions.models import Submission


class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ["attachment"]
        labels = {
            "attachment": "Add Work",
        }
