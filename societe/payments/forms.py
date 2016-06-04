from django import forms


class ChargeForm(forms.Form):

    """Docstring for ChargeForm. """
    stripe_token = forms.CharField()
