"""moeblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.shortcuts import render
from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin
from news import views


def faq(request):
    return render(request, 'faq/faq.html')


def team(request):
    return render(request, 'team/team.html')


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^faq/', faq, name='faq'),
    url(r'^team/', team, name='team'),
    url(r'^news/', include('news.urls')),
    url(r'^admin/', admin.site.urls),
]