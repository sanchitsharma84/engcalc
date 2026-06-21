from django.urls import path
from . import views


urlpatterns = [
    path('draglink_url', views.draglink_fcn, name='draglink_url_name')
]
