from django.urls import path
from . import views


urlpatterns = [
    path('rd_torque', views.rd_torque, name='rd_torque')
]