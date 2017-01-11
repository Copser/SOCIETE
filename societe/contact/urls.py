from django.conf.urls import url

from contact import views


urlpatterns = [
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^success/$', views.success, name="success"),
]
