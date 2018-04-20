"""Wechart URL Configuration

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
from werobot.contrib.django import make_view
from robot import robot
from . import view

urlpatterns = [
    url(r'^robot/',make_view(robot)),
    url(r'^joke/',view.get_joke),
    url(r'^neihan_video',view.get_video),
    url(r'^admin/', include(admin.site.urls)),
]
