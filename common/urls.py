from django.urls import path
from common import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test2/', views.test2, name='test2')
]