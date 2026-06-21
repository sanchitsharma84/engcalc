from django.urls import path
from . import views

urlpatterns = [
    path('rw_weight_url', views.rw_weight_fcn, name='rw_weight_url_name'),
]


