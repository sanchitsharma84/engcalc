from django.urls import path
from . import views

urlpatterns = [
    path('rw_bush_url', views.rw_bush_fcn, name='rw_bush_url_name'),
]


