from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.views.generic import TemplateView, FormView
from rest_framework.decorators import api_view

from .forms import LaborInfoForm, LaborReferenceForm, LaborExperienceForm, FutureLaborInfoForm

#Create your views here.
def index(request):
    """TODO: Docstring for index.
    :returns:

    """
    return render_to_response(
        'index.html',
        context_instance=RequestContext(request)
    )


class MainView(TemplateView):
    """TODO: Create MainView who will render forms
    return: TODO
    """
    template_name = 'apply_to/apply.html'


    def get(self, request, *args, **kwargs):
        """TODO: render all labor forms
        return: TODO
        """
        labor_form = LaborInfoForm(self.request.GET or None)
        labor_reference_form = LaborReferenceForm(self.request.GET or None)
        labor_experience_form = LaborExperienceForm(self.request.GET or None)
        labor_future_info_form = FutureLaborInfoForm(self.request.GET or None)
        context = self.get_context_data(**kwargs)
        context['labor_form'] = labor_form
        context['labor_reference_form'] = labor_reference_form
        context['labor_experience_form'] = labor_experience_form
        context['labor_future_info_form'] = labor_future_info_form
        return self.render_to_response(context)


class LaborInfoFormView(FormView):
    """TODO: Creating POST request for my LaborInfoForm
    return: TODO
    """
    form_class = LaborInfoForm
    template_name = 'apply_to/apply.html'
    success_url = '/success'

    def post(self, request, *args, **kwargs):
        """TODO: post request,
        return: TODO
        """
        labor_form = self.form_class(request.POST)
        labor_reference_form = LaborReferenceForm()
        labor_experience_form = LaborExperienceForm()
        labor_future_info_form = FutureLaborInfoForm()

        # validating form
        if labor_form.is_valid():
            labor_form.save()
            return self.render_to_response(
                self.get_context_data(
                    success=True
                )
            )
        else:
            return self.render_to_response(
            self.get_context_data(
                labor_form=labor_form,
                labor_reference_form=labor_reference_form,
                labor_experience_form=labor_experience_form,
                labor_future_info_form=labor_future_info_form
            )
        )


class LaborReferenceFormView(FormView):
    """TODO: Create POST request for LaborReferenceForm
    return: TODO
    """
    form_class = LaborReferenceForm
    template_name = 'apply_to/apply.html'
    success_url = '/success'

    def post(self, request, *args, **kwargs):
        """TODO: post request
        return: TODO
        """
        labor_form = LaborInfoForm()
        labor_reference_form = self.form_class(request.POST)
        labor_experience_form = LaborExperienceForm()
        labor_future_info_form = FutureLaborInfoForm()

        # validating form
        if labor_reference_form.is_valid():
            labor_reference_form.save()
            return self.render_to_response(
                self.get_context_data(
                    success=True
                )
            )
        else:
            return self.render_to_response(
            self.get_context_data(
                labor_form=labor_form,
                labor_reference_form=labor_reference_form,
                labor_experience_form=labor_experience_form,
                labor_future_info_form=labor_future_info_form
            )
        )


class LaborExperienceFormView(FormView):
    """TODO: Create POST request for LaborExperienceForm
    return: TODO
    """
    form_class = LaborExperienceForm
    template_name = 'apply_to/apply.html'
    success_url = '/success'

    def post(self, request, *args, **kwargs):
        """TODO: post request
        return: TODO
        """
        labor_form = LaborInfoForm(),
        labor_reference_form = LaborReferenceForm()
        labor_experience_form = self.form_class(request.POST)
        labor_future_info_form = FutureLaborInfoForm()

        # validating form
        if labor_experience_form.is_valid():
            labor_experience_form.save()
            return self.render_to_response(
                self.get_context_data(
                    success=True
                )
            )
        else:
            return self.render_to_response(
            self.get_context_data(
                labor_form=labor_form,
                labor_reference_form=labor_reference_form,
                labor_experience_form=labor_experience_form,
                labor_future_info_form=labor_future_info_form
            )
        )


class FutureLaborInfoFormView(FormView):
    """TODO: Create POST request for FutureLaborInfoForm
    return: TODO
    """
    form_class = FutureLaborInfoForm
    template_name = 'apply_to/apply.html'
    success_url = '/success'

    def post(self, request, *args, **kwargs):
        """TODO: post request
        return: TODO
        """
        labor_form = LaborInfoForm(),
        labor_reference_form = LaborReferenceForm()
        labor_experience_form = LaborExperienceForm
        labor_future_info_form = self.form_class(request.POST)

        # validating form
        if labor_future_info_form.is_valid():
            labor_future_info_form.save()
            return self.render_to_response(
                self.get_context_data(
                    success=True
                )
            )
        else:
            return self.render_to_response(
            self.get_context_data(
                labor_form=labor_form,
                labor_reference_form=labor_reference_form,
                labor_experience_form=labor_experience_form,
                labor_future_info_form=labor_future_info_form
            )
        )
