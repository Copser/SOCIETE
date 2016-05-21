from societe import settings
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView, TemplateView
from .forms import StripeForm


class StripeMixin(object):

    """Docstring for StripeMixin. """
    def get_context_data(self, **kwargs):
        """TODO: to be defined1. """
        context = super(StripeMixin, self).get_context_data(**kwargs)
        context['pubslishable_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context


class SuccessView(TemplateView):

    """Docstring for SuccessView. """
    template_name = 'payments/thank_you.html'


class StripePaymentsView(StripeMixin, FormView):

    """Docstring for StripePaymentsView. """
    tempalte_name = 'payments/subscribe.html'
    form_class = StripeForm
    success_url = reverse_lazy('thank_you')

    def form_valid(self, form):
        """TODO: to be defined1. """
        pass

    def form_invalid(self, form):
        """TODO: to be defined1. """
        pass
