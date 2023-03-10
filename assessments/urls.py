from django.urls import path
from . import views

app_name = "assessments"

urlpatterns = [
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.details, name="details"),
]
