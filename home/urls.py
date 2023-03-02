from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.home, name="index"),
    path("new-session/", views.new_session, name="student_form"),
    path("end-session/", views.end_session, name="end_session"),
    path("test-send-email/", views.test_send_email, name="test_send_email"),
]
