from django.urls import path
from . import views

urlpatterns = [
    path('rw_pressspeed_url', views.rw_pressspeed_fcn, name='rw_pressspeed_url_name'),
]


