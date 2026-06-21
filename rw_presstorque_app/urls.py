from django.urls import path
from . import views

urlpatterns = [
    path('rw_presstorque_url', views.rw_presstorque_fcn, name='rw_presstorque_url_name'),
]


