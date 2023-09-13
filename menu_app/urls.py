# menu_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_list, name='menu_list'),
]
