from django.urls import path
from . import views

urlpatterns = [
    path('rw_key_url', views.rw_key_fcn, name='rw_key_url_name'),
]


