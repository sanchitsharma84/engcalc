from django.urls import path
from . import views

urlpatterns = [
    path('rw_powerscrew_url', views.rw_powerscrew_fcn, name='rw_powerscrew_url_name'),
]


