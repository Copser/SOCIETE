"""superjobs URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from labor_apply.views import MainView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #
    # django-contrib-flatpages
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    # collect
    url(r'^$', 'labor_apply.views.index', name='index'),
#    url(r'^apply/$', 'labor.views.apply', name='apply'),
#    url(r'^success/$', 'labor.views.success', name='success'),
    #
    url(r'^apply/$', MainView.as_view(), name='apply'),

    url(r'^labor_apply/', include('labor_apply.urls')),
    #  Django Allauth
    url(r'^accounts/', include('allauth.urls')),
]
