# landing_page/views.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.
def index(request):
    """TODO: Setup simple view to render landing page
    return: TODO
    """
    return render_to_response(
        'index.html',
        context_instance=RequestContext(request)
    )

def about(request):
    """TODO: Setup simple view to render about page
    return: TODO
    """
    return render_to_response(
        'about.html',
        context_instance=RequestContext(request)
    )

def success(request):
    """TODO: create success views,
    we will display useful information for new jobs applicants
    return: TODO
    """
    return render_to_response(
        'success.html',
        context_instance=RequestContext(request)
)
