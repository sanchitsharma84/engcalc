from django.urls import path
from . import views


urlpatterns = [
    path('ecc_drive', views.ecc_drive, name='ecc_drive')
]