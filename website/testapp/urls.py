"""
URL Configuration for testapp
"""
from django.conf.urls import url

from testapp import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view()),
]
