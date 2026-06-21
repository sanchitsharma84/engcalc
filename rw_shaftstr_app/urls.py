from django.urls import path
from . import views

urlpatterns = [
    path('rw_shaftstr_url', views.rw_shaftstr_fcn, name='rw_shaftstr_url_name'),
]


