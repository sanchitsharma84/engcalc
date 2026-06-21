from django.urls import path
from . import views


urlpatterns = [
    path('link_drive', views.link_drive, name='link_drive')
]