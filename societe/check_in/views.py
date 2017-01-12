# check_in/views.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404,\
        render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import InitialCharacteristicModel
from .forms import InitialCharacteristicForm
# Create your views here.

#@login_required(login_url="someurl")
def arange(request):
    """TODO: Render InitialCharacteristicForm, nothing more,
    redirect to success/ page is form is valid if not trow
    and error, standard stuff
    return: TODO
    """
    if request.method == "POST":
        form = InitialCharacteristicForm(
            data=request.POST,
        )
        if form.is_valid():
            form.save(commit=False)
            return HttpResponseRedirect('/success/')
    else:
        form = InitialCharacteristicForm()

    return render_to_response(
        "check_in/arange.html",
        context_instance=RequestContext(
            request,
            {"form": form},
        )
    )

def success(request):
    """TODO: Render Success template, simple view, information
    template
    return: TODO
    """
    return render_to_response(
        "check_in/success.html",
        context_instance=RequestContext(
            request,
        )
    )
