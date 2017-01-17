# landing_page/views.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .forms import ContactUsView


def index(request):
    """TODO: Docstring for index.
    :returns: This function will return
    index.html(landing page), I should change the name to home page.

    """
#    layouts = OnMapReviewLayout.objects.filter(
#        category__codename='intern_review').order_by('?')
    return render_to_response(
        'index.html', context_instance=RequestContext(
            request,
#            {'selected_layout': layouts.first() if layouts else None}
        )
    )


def about(request):
    """TODO: Docstring for about page, simple view for about page.
    :returns: This function will return
    about.html(SOCIETE information)

    """
    if request.method == "POST":
        form = ContactUsView(request.POST)
        if form.is_valid():
            our_form = form.save(commit=False)
            our_form.save()
            messages.add_message(
                request, messages.INFO, "Your message has been sent, Thank you"
            )
            return HttpResponseRedirect('/')
    else:
        form = ContactUsView()
    t = loader.get_template('about.html')
    c = RequestContext(request, {'form': form})
    return HttpResponse(t.render(c))


def page_not_found(request):
    """TODO: Docstring for page_not_found.
    :returns: 404.html error template

    """
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def server_error(request):
    """TODO: Docstring for page_not_found.
    :returns: 500.html server error

    """
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response


def bad_request(request):
    """TODO: Docstring for page_not_found.
    :returns: 400.html bad_request

    """
    response = render_to_response('400.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 400
    return response


def permission_denied(request):
    """TODO: Docstring for page_not_found.
    :returns: 403.html permission denied

    """
    response = render_to_response('403.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 403
    return response
