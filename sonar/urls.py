"""sonar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from gcm.routers import router as gcm_router
# from sonar.logs import views
import sys
sys.path.append('/Users/Lucas/Desktop/embedded/sonar/logs')

import logs.views as logs_views

import sys
sys.path.append('/Users/Lucas/Desktop/embedded/sonar/distances')

import distances.views as distances_views

router = routers.DefaultRouter()
router.register(r'log', logs_views.LogViewSet)
router.register(r'distance', distances_views.DistanceViewSet)
router.register(r'devices', logs_views.CustomDevice)

urlpatterns = [
    url(r'^logs/', include('logs.urls', namespace="logs")),
    url(r'^distances/', include('distances.urls', namespace="distances")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]