from django.urls import path
from . import views


urlpatterns = [
    path('servo345cv', views.servo345cv, name='servo345cv')
]