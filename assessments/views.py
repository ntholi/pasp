from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from assessments.forms import AssessmentForm
from assessments.models import Assessment


@login_required
def details(request, pk):
    assessment = get_object_or_404(Assessment, pk=pk)
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
    course_id = request.GET.get("course", None)
    if course_id and request.method == "POST":
        form = AssessmentForm(request.POST, request.FILES)
        if form.is_valid():
            assessment = form.save(commit=False)
            assessment.course_id = course_id
            assessment.created_by = request.user
            assessment.save()
            return redirect("courses:details", pk=course_id)

    return render(request, "assessments/create.html", {"form": form})
