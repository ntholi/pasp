from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from datetime import timedelta

from assessments.models import Assessment
from submissions.forms import SubmissionForm
from submissions.models import Submission, Student


def get_or_create_student(request):
    student_name = request.COOKIES.get("student_name")
    student_number = request.COOKIES.get("student_number")
    student = Student.objects.get_or_create(
        student_number=student_number, defaults={"full_names": student_name}
    )
    return student[0]


def view(request, assessment_id):
    assessment = get_object_or_404(Assessment, pk=assessment_id)
    server_time = timezone.now() + timedelta(hours=2)

    if request.method == "POST":
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.assessment = assessment
            submission.student = get_or_create_student(request)
            submission.ip_address = request.META.get('REMOTE_ADDR')
            submission.save()
    else:
        form = SubmissionForm()

    context = {
        "form": form,
        "assessment": assessment,
        "submitted": request.method == "POST",
        "server_time": server_time,
    }
    return render(request, "submissions/view.html", context=context)
