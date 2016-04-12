from django.forms import ModelForm
from .models import ContactUsForm
from django import forms


class ContactUsView(ModelForm):

    """Docstring for ContactUsView. Registering form and fields for about page form,
        error_css_class and required_css_class are django style form errors
    """
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        """TODO: Registering form fields. """
        fields = ['name', 'email', 'phone_number', 'message']
        model = ContactUsForm
