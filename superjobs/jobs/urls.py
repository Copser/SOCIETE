from django.conf.urls import url

from jobs import views


urlpatterns = [
    url(r'^carpenterjobs/$', 'views.jobs.carpenterjobs', name='carpenterjobs')
]
