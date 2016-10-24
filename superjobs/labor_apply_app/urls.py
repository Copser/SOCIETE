from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from labor_apply_app import views

urlpatterns = [
    url(r'info/$', views.PersonalInfoViewList.as_view()),
    url(r'info/(?P<pk>[0-9]+)/$', views.PersonalInfoViewDetail()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
