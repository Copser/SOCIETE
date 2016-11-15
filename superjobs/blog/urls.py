from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from blog import views

urlpatterns = [

    url(r'^jobs/$', views.jobs, name='jobs'),
    url(r'^apply_to/$', views.apply_to, name='apply_to'),
    url(r'^success/$', views.success, name='success'),
    url(r'^(?P<slug>[\w|\-]+)/$', views.post, name='post'),

    url(r'^posts/$', views.post_list),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.post_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
