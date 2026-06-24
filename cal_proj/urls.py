"""cal_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from user_app import views as user_views
from django.conf.urls import url


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('this_site_administrator/', admin.site.urls),
    path('', include('user_app.urls')),
    path('add_app/', include('add_app.urls')),
    path('sub_app/', include('sub_app.urls')),
    path('block_weight_app/', include('block_weight_app.urls')),
    path('rd_toruqe_app/', include('rd_torque_app.urls')),
    path('ecc_drive_app/', include('ecc_drive_app.urls')),
    path('servo_345cv_app/', include('servo_345cv_app.urls')),
    path('servo345_app/', include('servo345_app.urls')),
    path('flywheel_app/', include('flywheel_app.urls')),
    path('link_drive_app/', include('link_drive_app.urls')),
    path('rw_weight_app/', include('rw_weight_app.urls')),
    path('rw_inertia_app/', include('rw_inertia_app.urls')),
    path('rw_gear_app/', include('rw_gear_app.urls')),
    path('rw_presstorque_app/', include('rw_presstorque_app.urls')),
    path('rw_pressspeed_app/', include('rw_pressspeed_app.urls')),
    path('rw_thread_app/', include('rw_thread_app.urls')),
    path('rw_powerscrew_app/', include('rw_powerscrew_app.urls')),
    path('rw_shaftstr_app/', include('rw_shaftstr_app.urls')),
    path('rw_ld_app/', include('rw_ld_app.urls')),
    path('rw_bush_app/', include('rw_bush_app.urls')),
    path('rw_bed_app/', include('rw_bed_app.urls')),
    path('rw_crown_app/', include('rw_crown_app.urls')),
    path('rw_slide_app/', include('rw_slide_app.urls')),
    path('rw_key_app/', include('rw_key_app.urls')),
    path('rw_sphcontact_app/', include('rw_sphcontact_app.urls')),
    path('rw_cylcontact_app/', include('rw_cylcontact_app.urls')),
    path('rw_gearstrength_app/', include('rw_gearstrength_app.urls')),
    path('draglink_app/', include('draglink_app.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='user_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user_app/logout.html'), name='logout'),
]
