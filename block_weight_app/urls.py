from django.urls import path
from . import views


urlpatterns = [
    path('block_weight_url', views.block_weight_fcn, name='block_weight_url_name')
]