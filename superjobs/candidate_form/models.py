# candidate_form/models.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from .choices import FIVE_BOROUGH, SKILL_CHOICE_TYPE, \
        TRAINING_CHOICE_FIELD, EXPERIENCE_CHOICE_TYPE, \
        WORK_HOURS_CHOICE_FIELD, WORK_PERMIT_CHOICE_FIELD, \
        DRIVERS_LICENSE_CHOICE_FIELD


# Create your models here.
class CandindateFormModel(models.Model):
    """TODO: Define Candidate model for future Candindate Form, this model
    is deffined of three part's Personal Information, Experience Information
    and Additional Information.
    This code will be reusable with python 2, choices fields will be added from
    choices.py

    In Personal Information we will make:
        - name - char field
        - last name - char field
        - email - email field
        - mobile phone number - integer field
        - confirm mobile phone number - we will add this later
                                        integer field
        - city - Once city for the beginning New York City
                but I will add choice field about which part
                of the NYC do you live?
                char field
        - street address - char field

    Experience Information will contain:
        - skill - choice field
        - candidate_paid_experience -  char field
        - candidate_hospitality_experience - char field
        - handyman_training - where did you get it - choice field
        - tool - text field
        - reference_letter - upload file field

    Other Information will contain:
        - work_hours - how many can you work contribute - choice field
        - payment_per_hour - decimal field
        - work_permit - choice field
        - drivers_license - choice field
        - upload_cv - upload file field
    return: TODO
    """
    first_name = models.CharField(
        _("Name"),
        max_length=225
    )
    last_name = models.CharField(
        _("Last Name"),
        max_length=225
    )
    email = models.EmailField(
        _("Email"),
        max_length=225,
        blank=True
    )
