# candidate_form/forms.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url, include

from candidate_form.views import ApplyFormView


urlpatterns = [
    url(r'^apply_form/$', ApplyFormView.as_view(), name='apply_form'),
]
