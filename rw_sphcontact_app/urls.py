from django.urls import path
from . import views

urlpatterns = [
    path('rw_sphcontact_url', views.rw_sphcontact_fcn, name='rw_sphcontact_url_name'),
]
