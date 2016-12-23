# blog/urls.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url, include

from blog import views

urlpatterns = [

    url(r'^jobs/$', views.jobs, name='jobs'),
    url(r'^apply_to/$', views.apply_to, name='apply_to'),
    url(r'^(?P<slug>[\w|\-]+)/$', views.post, name='post'),
]
