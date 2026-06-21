from django.urls import path
from . import views

urlpatterns = [
    path('rw_bed_url', views.rw_bed_fcn, name='rw_bed_url_name'),
]


