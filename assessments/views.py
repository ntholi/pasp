from django.shortcuts import render, redirect
from django.views import generic

from assessments.forms import AssessmentFormStep1, AssessmentFormStep2
from assessments.models import Assessment


def index(request):
    return render(request, "assessments/index.html")


def details(request, uuid):
    assessment = Assessment.objects.get(uuid=uuid)
    return render(request, "assessments/details.html", {"assessment": assessment})


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
            return redirect("assessments:details", uuid=assessment.uuid)
    return render(request, "assessments/create_step2.html", {"form": form})
