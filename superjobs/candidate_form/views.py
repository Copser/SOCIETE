# candidate_form/views.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

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
            form.save()
            return redirect("message_to_user_well_done")
    else:
        form = CandidateForm()

    return render(
        request,
        "candidate_apply.html",
        {"form": form},
    )
