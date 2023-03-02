from django.core.mail import send_mail

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from datetime import timedelta

from assessments.models import Assessment


def student_form(request):
    return render(request, "home/session_form.html")


def home(request):
    now = timezone.now() + timedelta(hours=2)
    if "student_name" in request.COOKIES and "student_number" in request.COOKIES:
        student_name = request.COOKIES.get("student_name")
        student_number = request.COOKIES.get("student_number")
        assessments = Assessment.objects.filter()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        context = {
            "student_name": student_name,
            "student_number": student_number,
            "time": dt_string,
            "assessments": assessments,
        }
        return render(
            request,
            "home/index.html",
            context,
        )
    else:
        return redirect("home:student_form")


def student_form(request):
    if request.method == "POST":
        student_name = request.POST.get("student_name")
        student_number = request.POST.get("student_number")
        response = redirect("home:index")
        response.set_cookie("student_name", student_name, max_age=60 * 60 * 8)
        response.set_cookie("student_number", student_number, max_age=60 * 60 * 8)
        return response
    return render(
        request,
        "home/session_form.html",
    )


def test_send_email(request):
    send_mail(
        "Subject here",
        "Here is the message.",
        "System Generated Messages",
        ["ntholi.g@gmail.com"],
        fail_silently=False,
    )
    return HttpResponse("Email Send, hopefully")
