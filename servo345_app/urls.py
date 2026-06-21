from django.urls import path
from . import views


urlpatterns = [
    path('servo345', views.servo345, name='servo345')
]