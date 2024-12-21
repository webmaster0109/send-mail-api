from django.urls import path
from .views import send_email_view


urlpatterns = [
    path("contact/", send_email_view, name="contact"),
]
