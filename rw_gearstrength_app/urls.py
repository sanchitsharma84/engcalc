from django.urls import path
from . import views

urlpatterns = [
    path('rw_gearstrength_url', views.rw_gearstrength_fcn, name='rw_gearstrength_url_name'),
]


