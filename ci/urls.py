from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^githookendpoint/$', views.hookendpoint, name='githookendpoint')
]