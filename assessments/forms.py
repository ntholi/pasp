from assessments.models import Assessment

from django import forms


class AssessmentFormStep1(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ["lecturer", "email"]


class AssessmentFormStep2(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ["course_name", "name", "start_time", "end_time", "question_paper"]
        labels = {
            "name": "Assessment Name",
        }
        widgets = {
            "start_time": forms.widgets.DateTimeInput(
                attrs={"type": "datetime-local", "class": "form-control"}
            ),
            "end_time": forms.widgets.DateTimeInput(
                attrs={"type": "datetime-local", "class": "form-control"}
            ),
        }

    question_paper = forms.FileField(
        label="Question Paper",
        required=False,
        widget=forms.ClearableFileInput(attrs={"accept": "application/pdf"}),
    )

    def clean_question_paper(self):
        question_paper = self.cleaned_data.get("question_paper", False)
        if question_paper:
            if question_paper.content_type != "application/pdf":
                raise forms.ValidationError("Only PDF files are allowed.")
            return question_paper
