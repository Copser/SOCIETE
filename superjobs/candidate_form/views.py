# candidate_form/views.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import FormView

from candidate_form.forms import CandidateForm

# Create your views here.
class CandidateFormView(FormView):
    """TODO: Render CandidateForm which will inherit from FormView
    return: TODO
    """
    template_name = 'candidate_form/candidate_apply.html'
    form_class = CandidateForm
    success_url = '/success/'

    def form_valid(self, form):
        """TODO: You need to pass objects from form and to
        cleaned_data method on them before you pass
        return super(CandidateForm, self).form_valid(form)
        return: TODO
        """
        return super(CandidateFormView, self).form_valid(form)
