from django import forms
from django.forms import inlineformset_factory, extras, ModelForm

from .models import LaborInfo


class LaborInfoForm(ModelForm):
    """TODO: Create form for are Labor, we are using inlineformset_factory, because
    we are rendering multiple forms
    return: TODO
    """
    birthdate = forms.DateField(widget=extras.SelectDateWidget(years=range(1975, 2010)))
    class Meta:
        model = LaborInfo
        fields = ['full_name', 'email', 'mobile', 'birthdate',
                  'previous_company_name', 'previous_company_email',
                  'previous_company_phone', 'previous_job_title',
                  'relevante_experience', 'hospitality',
                  'future_working_hourse', 'hourly_rate', 'drivers_license',
                  'curriculum_vitae']
