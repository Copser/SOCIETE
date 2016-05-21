from django import forms


class StripeForm(forms.Form):

    """Docstring for StripeForm. This for is simple, because we are going to use
        Stripe javascript code to support Stripe payments, this is all we need for
        stripe, everything else we will do with javascript.
        This will take care of building HTML form, validating user input, and securing
        customers card data. Sensitive credit card information is sent directly to Stripe
        and does not touch our server. Stripe returns to our site a token representation of the
        card, and this token can then be used in a charge request.
    """
    stripe_token = forms.CharField()
