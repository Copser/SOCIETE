from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

from .forms import ApplySuperView

# Create your views here.
def index(request):
    """TODO: Docstring for index.
    :returns:

    """
    return render_to_response(
        'index.html',
        context_instance=RequestContext(request)
    )


def apply(request):
    """TODO: Logic for labour application
    :returns: TODO
    """
    if request.method == 'POST':
        form = ApplySuperView(request.POST)
        if form.is_valid():
            labour_form = form.save(commit=False)
            labour_form.save()
            return HttpResponse('/success')

    else:
        form = ApplySuperView()
    return render_to_response(
        'apply.html', context_instance=RequestContext(
            request,
            {'form': form}
        )
    )


def success(request):
    """TODO: Success page
    :returns: TODO
    """
    return render(request, 'success.html')
