from django.urls import path
from . import views

urlpatterns = [
    path('rw_crown_url', views.rw_crown_fcn, name='rw_crown_url_name'),
]


