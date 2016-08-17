from django.shortcuts import render_to_response
from django.template import RequestContext

from reviews.models import OnMapReviewLayout


# Create your views here.
def newyork(request):
    """TODO: Docstring for newyork.
    :returns: TODO

    """
    return render_to_response(
        'newyork.html',
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

def apartments(request):
    """TODO: Docstring for newyork.
    :returns: TODO

    """
    layouts = OnMapReviewLayout.objects.filter(
        category__codename='intern_review').order_by('?')
    return render_to_response(
        'apartments.html', context_instance=RequestContext(
            request,
            {'selected_layout': layouts.first() if layouts else None}
        )
    )
