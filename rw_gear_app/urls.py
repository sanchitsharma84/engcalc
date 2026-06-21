from django.urls import path
from . import views

urlpatterns = [
    path('rw_gear_url', views.rw_gear_fcn, name='rw_gear_url_name'),
]


