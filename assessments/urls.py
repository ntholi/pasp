from django.urls import path
from . import views

app_name = "assessments"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create_step1, name="create"),
    path("create/step2/", views.create_step2, name="create_step2"),
    path("create-sucessful", views.create_successful, name="create_successful"),
    path("<str:pk>/", views.DetailView.as_view(), name="details"),
]
