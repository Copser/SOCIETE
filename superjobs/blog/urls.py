from django.conf.urls import url

from blog import views

urlpatterns = [

    url(r'^jobs/$', views.jobs, name='jobs'),
    url(r'^(?P<post_url>\w+)/$', views.post, name='post'),
    url(r'^apply/$', views.apply, name='apply'),

]
