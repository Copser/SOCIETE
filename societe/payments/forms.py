from django import forms
from django.core.exceptions import NON_FIELD_ERRORS


class PaymentForm(forms.Form):

    """Docstring for ChargeForm. """
    def addError(self, message):
        """TODO: Docstring for addError.
        :returns: TODO

        """
        self._errors[NON_FIELD_ERRORS] = self.error_class([message])


class CardForm(PaymentForm):

    """Docstring for CardForm. """
    name = forms.CharField(max_length=225, required=True)
    last_name = forms.CharField(max_length=225, required=True)
    email = forms.EmailField(required=True)
    last_4_digits = forms.CharField(
        required=True,
        min_length=4,
        max_length=4,
        widget=forms.HiddenInput()
    )
    stripe_token = forms.CharField(required=True, widget=forms.HiddenInput())

    class Meta:
        fields = ['name', 'last_name', 'email', 'last_4_digits']
