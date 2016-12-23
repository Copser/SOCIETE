# blog/api/urls.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from rest_framework import routers
from django.conf.urls import url, include
from . import views

router = routers.DefaultRouter()
router.register("job_posts", views.PostViewSet)

urlpatterns = [
    url(r'^posts/$',
        views.PostListView.as_view(),
        name='post_list'),
    url(r'posts/(?P<pk>\d+)/$',
        views.PostDetailView.as_view(),
        name='post_detail'),
    url(r'^', include(router.urls)),
]
