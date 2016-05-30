# from django.shortcuts import render
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
# from django.contrib.auth.decorators import login_required

from djstripe.models import Customer

from .forms import StripeForm
import stripe


class StripeMixin(object):

    """Docstring for StripeMixin. """
    def get_context_data(self, **kwargs):
        """TODO: to be defined1. """
        context = super(StripeMixin, self).get_context_data(**kwargs)
        context['pubslishable_key'] = settings.STRIPE_PUBLIC_KEY
        return context


class SuccessView(TemplateView):

    """Docstring for SuccessView. """
    template_name = 'thank_you.html'


class CustomerMixin(object):

    """Docstring for CustomerMixin. """
    def get_customer(self):
        """TODO: Docstring for get_customer.
        :returns: TODO

        """
        try:
            return self.request.user.customer
        except Exception:
            return Customer.create(self.request.user)


class StripePaymentsView(StripeMixin, CustomerMixin, FormView):

    """Docstring for StripePaymentsView. """
    template_name = 'subscribe.html'
    form_class = StripeForm
    success_url = reverse_lazy('thank_you')

    def form_valid(self, form):
        """TODO: to be defined1. """
        customer = self.get_customer()
        customer.update_card(form.cleaned_data.get('stripe_token', None))
        customer.subscribe('pro-yearly')

        return super(StripePaymentsView, self).form_valid(form)
