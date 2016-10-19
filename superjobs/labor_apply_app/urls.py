from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import TemplateView
from labor_apply_app import views

urlpatterns = [
    url(r'^$', 'labor_apply_app.views.index', name='index'),

    url(r'^apply_now/$', views.PersonalInfoCreateView.as_view()),
    url(r'^success/$', TemplateView.as_view()),
]
