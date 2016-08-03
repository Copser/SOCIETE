from django.conf.urls import include, url


urlpatterns = [
    url(r'^newyork/', 'cities.views.newyork', name='newyork'),
    url(r'^manila/', 'cities.views.manila', name='manila'),
    url(r'^istanbul/', 'cities.views.istanbul', name='istanbul'),
    url(r'^skopje/', 'cities.views.skopje', name='skopje'),
    url(r'^london/', 'cities.views.london', name='london'),
]
