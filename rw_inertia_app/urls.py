from django.urls import path
from . import views

urlpatterns = [
    path('rw_inertia_url', views.rw_inertia_fcn, name='rw_inertia_url_name'),
]


