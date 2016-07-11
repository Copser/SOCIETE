from django import forms
from django.core.exceptions import NON_FIELD_ERRORS


class PaymentForm(forms.Form):

    """Docstring for ChargeForm. """
    def addError(self, message):
        """TODO: Docstring for addError.
        :returns: TODO

        """
        self._errors[NON_FIELD_ERRORS] = self.error_class([message])


class SigninForm(PaymentForm):

    """Docstring for SigninForm. """
    email = forms.EmailField(required=True)
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(render_value=False)
    )


class CardForm(PaymentForm):

    """Docstring for CardForm. """
    last_4_digits = forms.CharField(
        required=True,
        min_length=4,
        max_length=4,
        widget=forms.HiddenInput()
    )
    stripe_token = forms.CharField(required=True, widget=forms.HiddenInput())


class UserForm(CardForm):

    """Docstring for PaymentUserForm. """
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(
        required=True,
        label=('Password'),
        widget=forms.PasswordInput(render_value=False)
    )
    ver_password = forms.CharField(
        required=True,
        label=('Verify Password'),
        widget=forms.PasswordInput(render_value=False)
    )

    def clean(self):
        """TODO: Docstring for clean.
        :returns: TODO

        """
        cleaned_data = self.cleaned_data
        password = cleaned_data.get('password')
        ver_password = cleaned_data.get('ver_password')
        if password != ver_password:
            raise forms.ValidationError('Password do not match')
        return cleaned_data
