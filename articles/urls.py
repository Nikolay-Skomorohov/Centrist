from articles import views
from django.urls import path

urlpatterns = [
    path("<int:article_id>/", views.article_page, name="article_page"),
]
