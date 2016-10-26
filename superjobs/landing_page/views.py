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
