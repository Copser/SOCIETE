from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.views.generic.edit import CreateView

from .forms import LaborInfoForm
from .models import LaborInfo

#Create your views here.
def index(request):
    """TODO: Docstring for index.
    :returns:

    """
    return render_to_response(
        'index.html',
        context_instance=RequestContext(request)
    )


class LaborInfoCreateView(CreateView):
    template_name = 'apply_to/apply.html'
    model = LaborInfo
    form_class = LaborInfoForm
    success_url = 'success/'

    def get(self, request, *args, **kwargs):
        """TODO: Handles GET request and instantiates blank versions of the form
        and its inline formsets
        return: TODO
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(
            self.get_context_data(form=form))


    def post(self, request, *args, **kwargs):
        """TODO: Handles POST request, instantiating a form instance and its inline
        formsets with the passed POST variables and then checing them for validity
        return: TODO
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self, form, *args, **kwargs):
        """TODO: Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredientes and Instructions and then redirexts to a success page
        return: TODO
        """
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, *args, **kwargs):
        """TODO: Called if a form is invalid. Re-renders the context data with the data-filled
        forms and errors
        return: TODO
        """
        return self.render_to_response(
            self.get_context_data(form=form))
