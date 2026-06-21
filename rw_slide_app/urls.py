from django.urls import path
from . import views

urlpatterns = [
    path('rw_slide_url', views.rw_slide_fcn, name='rw_slide_url_name'),
]


