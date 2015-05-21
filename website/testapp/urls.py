"""
URL Configuration for testapp
"""
from django.conf.urls import include, url

from testapp import views

urlpatterns = [
    url(r'^hello/(\w+)', views.hello),
    url(r'^$', views.home),
]
