from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse

from assessments.forms import AssessmentFormStep1, AssessmentFormStep2
from assessments.models import Assessment


def index(request):
    return render(request, "assessments/index.html")


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


def create_step1(request):
    initial_data = {
        "lecturer": request.session.get("lecturer", ""),
        "email": request.session.get("email", ""),
    }
    form = AssessmentFormStep1(initial=initial_data)
    if request.method == "POST":
        if "step1" in request.POST:
            form = AssessmentFormStep1(request.POST)
            if form.is_valid():
                request.session["lecturer"] = form.cleaned_data["lecturer"]
                request.session["email"] = form.cleaned_data["email"]
                return redirect("assessments:create_step2")
    return render(request, "assessments/create_step1.html", {"form": form})


def create_step2(request):
    lecturer = request.session.get("lecturer")
    email = request.session.get("email")

    if (not lecturer) or (not email):
        return redirect("assessments:create")

    form = AssessmentFormStep2()
    if request.method == "POST":
        form = AssessmentFormStep2(request.POST, request.FILES)
        if form.is_valid():
            assessment = form.save(commit=False)
            assessment.lecturer = lecturer
            assessment.email = email
            assessment.save()
            redirect_url = reverse("assessments:details", args=(assessment.uuid,))
            send_assessment_email(request, assessment)
            return redirect(f"{redirect_url}?newly_created=1")

    return render(request, "assessments/create_step2.html", {"form": form})


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
