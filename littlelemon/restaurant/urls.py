from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('index2/', views.index2, name='index2'),
    path('menu/', views.MenuItemView.as_view(), name='menu-items'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='single-menu-item'),
]