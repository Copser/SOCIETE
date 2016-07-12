# from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from django.contrib.auth.decorators import login_required

from .forms import CardForm
from .models import User

import stripe
import datetime

stripe.api_key = settings.TEST_SECRET_KEY


def soon():
    """TODO: Docstring for soon.
    :returns: TODO

    """
    soon = datetime.date.today() + datetime.timedelta(days=30)
    return {'month': soon.month, 'year': soon.year}


@login_required(login_url='/accounts/signup')
def register(request):
    """TODO: Docstring for sign_out.
    :returns: TODO

    """
    user = None
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():

            # update based on your billing method (subscription vs one time)
            # customer = stripe.Customer.create(
            #     email=form.cleaned_data['email'],
            #     description=form.cleaned_data['name'],
            #     card=form.cleaned_data['stripe_token'],
            #     plan="gold",
            # )

            customer = stripe.Charge.create(
                amount="30000",
                currency="usd",
                description=form.cleaned_data['email'],
                card=form.cleaned_data['stripe_token'],
            )

            user = User(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                last_4_digits=form.cleaned_data['last_4_digits'],
                stripe_id=customer.id,
            )

            return HttpResponseRedirect('/thank_you')
    else:
        form = CardForm()

    return render_to_response(
        'register.html',
        {
            'form': form,
            'months': range(1, 12),
            'publishable': settings.TEST_PUBLISHABLE_KEY,
            'soon': soon(),
            'user': user,
            'years': range(2011, 2036),
        },
        context_instance=RequestContext(request)
    )


def thank_you(request):
    """TODO: Docstring for thank_you.
    :returns: TODO

    """
    return render_to_response(
        'thank_you.html',
        context_instance=RequestContext(request))
