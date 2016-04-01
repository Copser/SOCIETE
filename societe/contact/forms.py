from django.forms import ModelForm, extras
from .models import ContactForm
from django import forms
from django_countries.widgets import CountrySelectWidget
import datetime


def get_move_date_field():
    """TODO: Docstring for get_move_date_field.
    :returns: return a DateField suitable for move_in_date and move_out_date

    """
    return forms.DateField(widget=extras.SelectDateWidget(), initial=datetime.date.today())


class ContactView(ModelForm):

    """TODO: Docstring for ContactView.
    :returns: ContactView is a class in which we are returning about user information.
        error_css_class and required_css_class are django style form errors
    """
    error_css_class = 'error'
    required_css_class = 'required'
    birthday = forms.DateField(widget=extras.SelectDateWidget(years=range(2010, 1939, -1)))
    move_in_date = get_move_date_field()
    move_out_date = get_move_date_field()

    class Meta:
        fields = ['first_name', 'last_name', 'email', 'mobile',
                  'birthday', 'move_in_date', 'move_out_date',
                  'country', 'message']
        model = ContactForm
        widgets = {
            'country': CountrySelectWidget()
        }
