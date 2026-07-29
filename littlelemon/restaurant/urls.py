from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('index2/', views.index2, name='index2'),
]