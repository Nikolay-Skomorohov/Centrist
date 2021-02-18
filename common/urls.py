from django.urls import path
from common import views

urlpatterns = [
    path("", views.home, name="home"),
    path("categories/", views.categories, name="categories"),
    path("gallery/", views.gallery, name="gallery"),
    path("about/", views.about, name="about"),
    path("profile/", views.profile, name="profile"),
]
