from django.urls import path
from .views import send_email_view


urlpatterns = [
    path("sponsor-mail-form/", send_email_view, name="contact"),
]
