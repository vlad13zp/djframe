"""
URL Configuration for testapp
"""
from django.conf.urls import url

from testapp import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^user/(\d+)', views.info),
]
