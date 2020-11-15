from django.urls import path
from common import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.categories, name='categories'),
    path('gallery/', views.gallery, name='gallery'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
]