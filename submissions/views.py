from django.shortcuts import render, get_object_or_404
from django.utils import timezone
import pytz

from assessments.models import Assessment
from submissions.forms import SubmissionForm
from submissions.models import Student, Submission


def get_or_create_student(request):
    student_name = request.COOKIES.get("student_name")
    student_number = request.COOKIES.get("student_number")
    student = Student.objects.get_or_create(
        student_number=student_number,
        defaults={"full_names": student_name, "student_number": student_number},
    )
    return student[0]


def index(request, assessment_id):
    assessment = get_object_or_404(Assessment, pk=assessment_id)
    now = timezone.now().astimezone(pytz.timezone("Africa/Maseru"))
    alert = None

    if request.method == "POST":
        student = get_or_create_student(request)
        form = __create_student_submission(request, student, assessment)
        alert = {
            "message": f"{assessment.title} Submitted Successfully",
            "type": "alert-success",
        }
    else:
        form = SubmissionForm()

    context = {
        "form": form,
        "assessment": assessment,
        "submitted": request.method == "POST",
        "server_time": now,
        "alert": alert,
    }
    return render(request, "submissions/index.html", context=context)


def __create_student_submission(request, student, assessment):
    form = SubmissionForm(request.POST, request.FILES)
    if form.is_valid():
        submission_id = f"{assessment.id}_{student.student_number}"
        submission, created = Submission.objects.get_or_create(
            id=submission_id,
            defaults={
                "assessment": assessment,
                "student": student,
                "attachment": request.FILES["attachment"],
                "ip_address": request.META.get("REMOTE_ADDR"),
            },
        )
        if not created:
            submission.submission_times += 1
        submission.save()
    return form
