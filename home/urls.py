from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.home, name="index"),
    path('new-session/', views.student_form, name='student_form'),
    path("test-send-email/", views.test_send_email, name="test_send_email"),
]
