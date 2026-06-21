from django.urls import path
from . import views

urlpatterns = [
    path('rw_cylcontact_url', views.rw_cylcontact_fcn, name='rw_cylcontact_url_name'),
]
