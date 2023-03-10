from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    path("", views.CourseListView.as_view(), name="index"),
    path("<int:pk>/", views.course_details, name="details"),
    path("create/", views.create_course, name="create"),
    path("<int:pk>/update/", views.CourseUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.CourseDeleteView.as_view(), name="delete"),
]
