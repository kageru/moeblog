from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.blog, name='blog'),
    url(r'^(?P<tag_name>\w*)/$', views.blogfilter, name='blogfilter')
]
