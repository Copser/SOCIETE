from django.shortcuts import render_to_response
from django.template import RequestContext


# Create your views here.
def newyork(request):
    """TODO: Docstring for newyork.
    :returns: TODO

    """
    return render_to_response(
        'newyork.html',
        context_instance=RequestContext(request)
    )


def manila(request):
    """TODO: Docstring for newyork.
    :returns: TODO

    """
    return render_to_response(
        'manila.html',
        context_instance=RequestContext(request)
    )


def istanbul(request):
    """TODO: Docstring for newyork.
    :returns: TODO

    """
    return render_to_response(
        'istanbul.html',
        context_instance=RequestContext(request)
    )


def skopje(request):
    """TODO: Docstring for newyork.
    :returns: TODO

    """
    return render_to_response(
        'skopje.html',
        context_instance=RequestContext(request)
    )


def london(request):
    """TODO: Docstring for london.
    :returns: TODO

    """
    return render_to_response(
        'london.html',
        context_instance=RequestContext(request)
    )
