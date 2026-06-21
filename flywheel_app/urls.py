from django.urls import path
from . import views


urlpatterns = [
    path('flywheel', views.flywheel, name='flywheel')
]