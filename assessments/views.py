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
def details(request, pk):
    assessment = Assessment.objects.get(pk)
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
            assessment.course_id = request.session.get("course", None)
            assessment.created_by = request.user
            assessment.save()
            redirect_url = reverse("assessments:details", args=(assessment.id,))
            return redirect(f"{redirect_url}?newly_created=1")

    return render(request, "assessments/create.html", {"form": form})
