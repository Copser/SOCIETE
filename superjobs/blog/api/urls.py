# blog/api/urls.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^posts/$',
        views.PostListView.as_view(),
        name='post_list'),
    url(r'posts/(?P<pk>\d+)/$',
        views.PostDetailView.as_view(),
        name='post_detail'),
]
