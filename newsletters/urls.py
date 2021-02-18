from django.urls import path
from newsletters import views

urlpatterns = [
    path("", views.newsletter, name="newsletter"),
]
