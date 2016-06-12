from django import forms


class BrainChargeForm(forms.Form):

    """Docstring for BrainCharge_form. Create custom Erasmus Charge for which we will
    connect with BrainTreePayments.
    """
    braintree_token = forms.CharField()
