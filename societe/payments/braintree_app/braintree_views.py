from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext

import braintree
from .braintree_forms import BrainChargeForm


# BrainTree Configuration
braintree.Configuration.configure(braintree.Environment.Sandbox,
                                  merchant_id=settings.BRAINTREE_MERCHANT_ID,
                                  public_key=settings.BRAINTREE_PUBLIC_KEY,
                                  private_key=settings.BRAINTREE_PRIVATE_KEY)


def braintree_token(request):
    """TODO: Docstring for braintree_token.
    :returns: TODO

    """
    if request.method == 'GET':
        request.session['braintree_client_token'] = braintree.ClientToken.generate()
        return render(request, 'braintree_templates/braintree_payment.html')
    else:
        if request.method == 'POST':
            form = BrainChargeForm(request.POST)
            if form.is_valid():
                client_nounce = request.form['payment_method_nounce']
                braintree_charge = braintree.Transaction.sale({
                    "amount": "300.00",
                    "payment_method_nounce": client_nounce,
                    "options": {
                        "submit_for_settlemant": True
                    }
                })
            else:
                return HttpResponseRedirect('/sucess')
        else:
            form = BrainChargeForm()

    return render_to_response('braintree_templates/braintree_payment.html', {
                              'form': form,
                              'braintree_charge': braintree_charge,
                              },
                              context_instance=RequestContext(request))
