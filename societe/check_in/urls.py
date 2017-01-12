# check_in/urls.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include

from check_in import views


urlpatterns = [
    url(r'^arange/$', views.arange, name='arange'),
    url(r'^success/$', views.success, name='success'),
]
