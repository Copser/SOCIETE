# candidate_form/views.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import FormView

from candidate_form.forms import CandidateForm

# Create your views here.
class ApplyFormView(FormView):
    """TODO: Render CandidateForm which will inherit from FormView
    return: TODO
    """
    tempate_name = 'candidate_form/candidate_apply.html'
    form_class = CandidateForm
