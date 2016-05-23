from societe import settings
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from .forms import StripeForm
import stripe


class StripeMixin(object):

    """Docstring for StripeMixin. """
    def get_context_data(self, **kwargs):
        """TODO: to be defined1. """
        context = super(StripeMixin, self).get_context_data(**kwargs)
        context['pubslishable_key'] = settings.TEST_PUBLISHABLE_KEY
        return context


class SuccessView(TemplateView):

    """Docstring for SuccessView. """
    template_name = 'thank_you.html'


class StripePaymentsView(StripeMixin, FormView):

    """Docstring for StripePaymentsView. """
    template_name = 'subscribe.html'
    form_class = StripeForm
    success_url = reverse_lazy('thank_you')

    def form_valid(self, form):
        """TODO: to be defined1. """
        stripe.api_key = settings.TEST_SECRET_KEY

        customer_data = {
            'description': 'Some Customer Data',
            'card': form.cleaned_data['stripe_token']
        }
        customer = stripe.Customer.create(**customer_data)

        # chose a plane for the cusotmer
        customer.subscriptions.create(plan='basic_plan')

        return super(StripePaymentsView, self).form_valid(form)
