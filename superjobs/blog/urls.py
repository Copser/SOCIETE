# blog/forms.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from blog import views

urlpatterns = [

    url(r'^posts/$', views.posts_list),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.posts_detail),

#    url(r'^users/$', views.UserList.as_view()),
#    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),

    url(r'^jobs/$', views.jobs, name='jobs'),
    url(r'^apply_to/$', ApplyFormView.as_view(), name='apply_to'),
#    url(r'^apply_to/$', views.apply_to, name='apply_to'),
    url(r'^success/$', views.success, name='success'),
    url(r'^(?P<slug>[\w|\-]+)/$', views.post, name='post'),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
