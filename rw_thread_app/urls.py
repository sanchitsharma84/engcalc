from django.urls import path
from . import views

urlpatterns = [
    path('rw_thread_url', views.rw_thread_fcn, name='rw_thread_url_name'),
]


