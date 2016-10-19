from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.views.generic.edit import FormView

from .forms import PersonalInfoForm
from .models import PersonalInfo

#Create your views here.
def index(request):
    """TODO: Landing Page
    return: TODO
    """
    return render_to_response(
        'index.html',
        context_instance=RequestContext(request)
    )


class PersonalInfoCreateView(FormView):
    """TODO: CreateView for PersonalInfoForm
    return: TODO
    """
    template_name = 'apply_to/apply_now.html'
    form_class = PersonalInfoForm
    success_url = 'success/'

    def get(self, form):
        """TODO: define get request
        return: TODO
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(
            self.get_context_data(form=form))

    def post(self, form):
        """TODO: Post request for PersonalInfoForm
        return: TODO
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_class(form)

    def form_valid(self, form):
        """TODO: Validate form
        return: TODO
        """
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """TODO: handle invalid form request
        return: TODO
        """
        return self.render_to_response(
            self.get_context_data(form=form))
