from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext, loader

from paypal.pro.views import PayPalPro

from .forms import ChargeForm
import stripe


# PayPal section
def nvp_handler(nvp):
    """TODO: Docstring for nvp_handler.
    :returns: This is passed  a PayPalNVP object when payment succeeds.

    """
    pass


def erasums_charge(request):
    """TODO: Docstring for erasums_charge.
    :returns: TODO

    """
    item = {
        "paymentrequest_0_atm": "300.00",  # charge
        "inv": "inventory",  # unique tracking variable paypal
        "custom": "tracking",  # custom tracking variable for you
        "cancelurl": "",  # express checkout cancel url
        "returnurl": ""  # express checkout return url
    }

    ppp = PayPalPro(
        item=item,
        payment_template="payment.html",
        confirm_tempalte="confirmation.html",
        success_url="/success",
        nvp_handler=nvp_handler)
    return ppp(request)


# Stripe section
def charge(request):
    """TODO: Docstring for charge.
    :returns: Charge view is responsible for providing us with user token, which we will
    then send to Stripe so we don't store any sensitive information inside are database,
    and are application.
    Cusomer information will be stored on https://stripe.com/, we are following PCI compile
    principle inside Erasmus application.

    """
    publishable_key = settings.TEST_PUBLISHABLE_KEY
    if request.method == 'POST':
        form = ChargeForm(request.POST)
        if form.is_valid():
            # Get the credit card details submitet by the form
            token = request.POST['stripeToken']

            try:
                charge = stripe.Charge.create(
                    amonut=30000,
                    currency="usd",
                    source=token,
                    description="Erasmus Charge"
                )
            except stripe.error.Card as e:
                # The card hase been descilend
                raise
        else:
            return HttpResponseRedirect('/thank_you')
    else:
        form = ChargeForm()
    t = loader.get_template('charge.html')
    c = RequestContext(request, {'publishable_key': publishable_key, })
    return HttpResponse(t.render(c))


def thank_you(request):
    """TODO: Docstring for thank_you.
    :returns: TODO

    """
    return render(request, 'thank_you.html')
