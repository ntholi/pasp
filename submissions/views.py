from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from datetime import timedelta

from assessments.models import Assessment
from submissions.forms import SubmissionForm
from submissions.models import Submission


def view(request, assessment_id):
    assessment = get_object_or_404(Assessment, pk=assessment_id)
    server_time = timezone.now() + timedelta(hours=2)
    submitted = False

    if request.method == "POST":
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.assessment = assessment
            submission.save()
            submitted = True
    else:
        form = SubmissionForm()

    context = {
        "form": form,
        "assessment": assessment,
        "submitted": submitted,
        "server_time": server_time,
    }
    return render(request, "submissions/view.html", context=context)
