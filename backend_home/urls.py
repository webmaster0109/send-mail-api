from django.urls import path
from .views import *


urlpatterns = [
    path("sponsor-mail-form/", send_email_view, name="contact"),
    path("contact-form/", contact_form_views, name="contact"),
    path("subscribe/", subscribe_view, name="subscribe"),
]
