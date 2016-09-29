from django.shortcuts import render, render_to_response
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from rest_framework.decorators import api_view

from labor.forms import ApplyFormView

# Create your views here.
def index(request):
    """TODO: Docstring for index.
    :returns:

    """
    return render_to_response(
        'index.html',
        context_instance=RequestContext(request)
    )

@api_view(['GET', 'POST'])
def apply(request):
    """TODO: crete view with rest_framework api_view decorator
    return: TODO
    """
    if request.method == 'POST':
        form = ApplyFormView(request.POST)
        if form.is_valid():
            apply_form = form.save(commit=False)
            apply_form.save()
            return Response('/success')

    else:
        form = ApplyFormView()
    return Response('apply.html', {'form': form})

def success(request):
    """TODO: Success page
    :returns: TODO
    """
    return render(request, 'success.html')
