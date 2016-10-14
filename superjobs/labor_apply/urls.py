from django.conf.urls import url
from django.views.generic import TemplateView

from labor_apply.views import LaborInfoCreateView

urlpatterns = [
    url(r'^$', 'labor_apply.views.index', name='index'),
    url(r'^apply/$', LaborInfoCreateView.as_view()),
    url(r'^success/$', TemplateView.as_view()),
]
