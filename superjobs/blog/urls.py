from django.conf.urls import url

from blog import views

urlpatterns = [

    url(r'^jobs/$', views.jobs, name='jobs'),

]
