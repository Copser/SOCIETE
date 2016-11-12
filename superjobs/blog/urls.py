from django.conf.urls import url

from blog import views

urlpatterns = [

    url(r'^jobs/$', views.jobs, name='jobs'),
    url(r'^(?P<slug>[\w|\-]/$', views.post, name='post'),
    url(r'^apply_to/$', views.apply_to, name='apply_to'),

]
