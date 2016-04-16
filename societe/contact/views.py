from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext, loader
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import ContactView


# Create your views here.
@login_required(login_url='/accounts/signup')
def contact(request):
    """TODO: Docstring for contact.This will be a contact app
    for the SOCIETE aplicant's, they will be asked to write down,
    what is the budget is available for them, and for how much
    money they want to find an apartment.
    :returns: TODO

    """
    if request.method == 'POST':
        form = ContactView(request.POST)
        if form.is_valid():
            our_form = form.save(commit=False)
            our_form.save()
            messages.add_message(
                request, messages.INFO, 'Your message has been\
                    sent. Thank you.'
            )
            return HttpResponseRedirect('/success')
    else:
        form = ContactView()
    t = loader.get_template('contact.html')
    c = RequestContext(request, {'form': form, })
    return HttpResponse(t.render(c))


def success(request):
    """TODO: Docstring for success.
    :returns: TODO

    """
    return render(request, 'success.html')
