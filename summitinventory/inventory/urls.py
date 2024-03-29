"""inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('get/', views.get_product),
    path('list/', views.list_all_products),
    path('add/', views.add_product),
    re_path(r'^update/(?P<id>\d{1,5000})/$', views.update_product),
    re_path(r'^delete/soft/(?P<id>\d{1,5000})/$', views.soft_delete_product),
    re_path(r'^delete/hard/(?P<id>\d{1,5000})/$', views.hard_delete_product),
    re_path(r'^restore/(?P<id>\d{1,5000})/$', views.restore_product),
    
]