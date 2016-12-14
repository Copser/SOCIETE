# candidate_form/forms.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url, include

from candidate_form.views import CandidateFormView


urlpatterns = [
    url(r'^apply_form/$', CandidateFormView.as_view(), name='apply_form'),
]
