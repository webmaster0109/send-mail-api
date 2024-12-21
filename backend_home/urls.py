from django.urls import path
from .views import send_email_view


urlpatterns = [
    path("send-mail/", send_email_view, name="contact"),
]
