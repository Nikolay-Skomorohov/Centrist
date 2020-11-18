from django.urls import path
from newsletters import views

urlpatterns = [
    path('newsletter/', views.newsletter, name='newsletter'),
]
