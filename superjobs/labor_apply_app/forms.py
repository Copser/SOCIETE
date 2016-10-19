from django import forms
from django.forms import extras, ModelForm

from .models import PersonalInfo


class PersonalInfoForm(ModelForm):
    """TODO: Create form
    return: TODO
    """
    birthdate = forms.DateField(widget=extras.SelectDateWidget(years=range(1975, 2010)))
    class Meta:
        model = PersonalInfo
        fields = ['full_name', 'email', 'mobile', 'birthdate',
                  'previous_company_name', 'previous_company_email', 'previous_company_phone',
                  'previous_job_title',
                  'relevante_experience', 'hospitality_experience',
                  'future_working_hours', 'hourly_wage', 'driver_license', 'curriculum_vitae']

        def __init__(self, *args, **kwargs):
            super(PersonalInfoForm, self).__init__(*args, **kwargs)
