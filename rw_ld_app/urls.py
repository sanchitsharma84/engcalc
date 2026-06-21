from django.urls import path
from . import views

urlpatterns = [
    path('rw_ld_url', views.rw_ld_fcn, name='rw_ld_url_name'),
]


