from assessments.models import Assessment

from django import forms


class AssessmentFormStep1(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ["lecturer", "email"]


class AssessmentFormStep2(forms.ModelForm):
    attachment = forms.FileField(
        widget=forms.FileInput(attrs={"question_paper": "application/pdf"})
    )

    class Meta:
        model = Assessment
        fields = [
            "title",
            "course_name",
            "course_code",
            "question_paper",
            "start_time",
            "end_time",
        ]
        widgets = {
            "course_code": forms.widgets.TextInput(attrs={"placeholder": "(Optional)"}),
            "start_time": forms.widgets.DateTimeInput(
                attrs={"type": "datetime-local", "class": "form-control"}
            ),
            "end_time": forms.widgets.DateTimeInput(
                attrs={"type": "datetime-local", "class": "form-control"}
            ),
        }
