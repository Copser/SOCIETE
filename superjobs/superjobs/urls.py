"""superjobs URL Configuration

the `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
examples:
function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^admin/', include(admin.site.urls)),
        # django-contrib-flatpages

        # url(r'^apply_to/', include('labor_apply_app.urls')),
        url(r'^$', 'landing_page.views.index', name='index'),
        url(r'^about/$', 'landing_page.views.about', name='about'),


        #  Django Allauth
        url(r'^accounts/', include('allauth.urls')),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
