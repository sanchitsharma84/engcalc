from django.urls import path
from . import views


urlpatterns = [
    path('', views.home4all, name='home-all'),
    path('home_users', views.home4users, name='home-users'),
]