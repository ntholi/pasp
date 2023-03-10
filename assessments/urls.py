from django.urls import path
from . import views

app_name = "assessments"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<str:uuid>/", views.details, name="details"),
]
