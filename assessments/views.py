from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse

from assessments.forms import AssessmentForm
from assessments.models import Assessment


@login_required
def index(request):
    return render(request, "assessments/index.html")


@login_required
def details(request, uuid):
    assessment = Assessment.objects.get(uuid=uuid)
    if not assessment:
        raise Http404("Assessment does not exist")
    submissions = assessment.submission_set.all()
    return render(
        request,
        "assessments/details.html",
        {
            "assessment": assessment,
            "submissions": submissions,
            "newly_created": request.GET.get("newly_created", 0),
        },
    )


@login_required
def create(request):
    form = AssessmentForm()
    course = request.GET.get("course", None)
    if course:
        request.session["course"] = course
    if request.method == "POST":
        form = AssessmentForm(request.POST, request.FILES)
        if form.is_valid():
            assessment = form.save(commit=False)
            assessment.lecturer = request.user
            assessment.save()
            redirect_url = reverse("assessments:details", args=(assessment.uuid,))
            send_assessment_email(request, assessment)
            return redirect(f"{redirect_url}?newly_created=1")

    return render(request, "assessments/create.html", {"form": form})


def send_assessment_email(request, assessment):
    # Generate the assessment details URL
    assessment_url = request.build_absolute_uri(
        reverse("assessments:details", args=[str(assessment.uuid)])
    )

    message = f"Dear {assessment.lecturer},\n\n"
    message += f"Please find below the details of the assessment you created:\n\n"
    message += f"Secret Id: {assessment.uuid}\n"
    message += f"Title: {assessment.name}\n"
    message += f"Course Name: {assessment.course_name}\n\n"
    message += f"Click the link below to view the assessment details:\n"
    message += f"{assessment_url}\n\n"
    message += "Best regards,\n"
    message += "PASP Automated System"

    # Send the email
    send_mail(
        subject="PASP Assessment Details",
        message=message,
        from_email="PASP",
        recipient_list=[assessment.email],
        fail_silently=True,
    )
