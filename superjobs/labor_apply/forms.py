from django import forms
from django.forms import formset_factory, extras

from .models import LaborInfo, FutureLaborInfo, LaborReference, LaborExperience, DRIVERS_CATEGORY_CHOICES

class LaborInfoForm(forms.Form):
    """TODO: Initialize LaborInfoForm
    return: TODO
    """
    birthdate = forms.DateField(widget=extras.SelectDateWidget(years=range(1975, 2010)))
    class Meta:
        model = LaborInfo
        fields = ['full_name', 'email', 'mobile', 'birthdate']


class LaborReferenceForm(forms.Form):
    """TODO: extending with form sets
    return: TODO
    """
    LaborReferenceSet = formset_factory(LaborReference, extra=5, max_num=3)

    class Meta:
        model = LaborReference
        fields = ['company_name', 'company_email', 'company_phone', 'previous_job_title']


class LaborExperienceForm(forms.Form):
    """TODO: extend TextField
    return: TODO
    """
    relevante_experience = forms.CharField(widget=forms.Textarea)
    hospitality = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = LaborExperience
        fields = ['relevante_experience', 'hospitality']


class FutureLaborInfoForm(forms.Form):
    """TODO: multiple choice field,
    return: TODO
    """
    drivers_license = forms.CharField(
        max_length=6,
        widget=forms.Select(choices=DRIVERS_CATEGORY_CHOICES),
    )
    class Meta:
        model = FutureLaborInfo
        fields = ['future_working_hourse', 'hourly_rate', 'drivers_license', 'curriculum_vitae']
        widget = {
            'future_working_hourse': forms.NumberInput(attrs={'step': 5.0}),
        }
