# candidate_form/views.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext

from candidate_form.forms import CandidateForm

# Create your views here.
# @login_required
def apply_for_job(request):
    if request.method == "POST":
        form = CandidateForm(
            data=request.POST,
            files=request.FILES,
        )
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            messages.add_message(
                request, messages.INFO, "You have applied, Thank you!"
            )
            return HttpResponseRedirect("/success")
        else:
            print(form.errors)
    else:
        form = CandidateForm()

    t = loader.get_template('candidate_apply.html')
    c = RequestContext(
        request,
        {
            'form': form
        }
    )
    return HttpResponse(t.render(c))
