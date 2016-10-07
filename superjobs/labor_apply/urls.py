from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^apply/$', TemplateView.as_view()),
    url(r'^success/$', TemplateView.as_view()),
]
