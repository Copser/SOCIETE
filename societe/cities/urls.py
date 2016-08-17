from django.conf.urls import include, url


urlpatterns = [
    url(r'^newyork/', 'cities.views.newyork', name='newyork'),
    url(r'^skopje/', 'cities.views.skopje', name='skopje'),
    url(r'^apartments/', 'cities.views.apartments', name='apartments'),
]
