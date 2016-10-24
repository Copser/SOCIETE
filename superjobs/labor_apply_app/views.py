from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.views.generic.edit import CreateView

from rest_framework.views import APIView
from rest_framework.response import Response

from .forms import PersonalInfoForm

#Create your views here.
def index(request):
    """TODO: Landing Page
    return: TODO
    """
    return render_to_response(
        'index.html',
        context_instance=RequestContext(request)
    )


class PersonalInfoView(CreateView):
    """TODO: CreateView for PersonalInfoForm
    return: TODO
    """
    template_name = 'apply_now.html'
    form_class = PersonalInfoForm
    success_url = 'success/'

    def form_valid(self, form, *args, **kwargs):
        """TODO: Validate form
        return: TODO
        """
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, *args, **kwargs):
        """TODO: handle invalid form request
        return: TODO
        """
        return self.render_to_response(
            self.get_context_data(form=form))


class PersonalInfoViewList(APIView):
    """TODO:
    return: TODO
    """
    pass


class PersonalInfoViewDetail(APIView):
    """TODO:
    return: TODO
    """
    pass
