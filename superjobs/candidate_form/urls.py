# candidate_form/forms.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url, include

from candidate_form import views


urlpatterns = [
    url(r'^apply_for_job/$', views.apply_for_job, name='apply_for_job'),
]
