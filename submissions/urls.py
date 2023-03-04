from django.urls import path
from . import views

app_name = "submissions"

urlpatterns = [
    path(
        "<int:assessment_id>/",
        views.index,
        name="index",
    ),
]
