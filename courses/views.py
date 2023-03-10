from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import CourseForm
from .models import Course
from django.urls import reverse_lazy


def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('courses:index')
    else:
        form = CourseForm()
    return render(request, "courses/create.html", {'form': form})


def course_details(request, pk):
    course = Course.objects.get(pk=pk)
    assessments = course.assessment_set.all()
    return render(request, "courses/details.html", {'course': course, 'assessments': assessments})


class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = "courses/index.html"
    ordering = ["-created_at"]
    context_object_name = "courses"

    def get_queryset(self):
        return Course.objects.filter(lecturers=self.request.user)


class CourseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Course
    template_name = "courses/update.html"
    fields = ["name", "code"]

    def test_func(self):
        course = self.get_object()
        return self.request.user in course.lecturers.all()


class CourseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Course
    template_name = "courses/delete.html"
    success_url = reverse_lazy("courses:index")

    def test_func(self):
        course = self.get_object()
        return self.request.user in course.lecturers.all()
