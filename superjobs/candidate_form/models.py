# candidate_form/models.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import RegexValidator

from utils.choices import FIVE_BOROUGH, SKILL_CHOICE_TYPE, \
        TRAINING_CHOICE_FIELD, EXPERIENCE_CHOICE_TYPE, \
        WORK_HOURS_CHOICE_FIELD, WORK_PERMIT_CHOICE_FIELD, \
        DRIVERS_LICENSE_CHOICE_FIELD
from utils.fields import MultilingualCharField, \
        MultilingualTextField


# Create your models here.
@python_2_unicode_compatible
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
        - confirm mobile phone number - we will use twillio
        - city - Once city for the beginning New York City
                but I will add choice field about which part
                of the NYC do you live?
                choices
        - street address - char field

    Experience Information will contain:
        - skill - choices
        - candidate_experience -  choices
        - candidate_hospitality_experience - char field
        - handyman_training - where did you get it - choices
        - tool - text field
        - reference_letter - upload file field

    Other Information will contain:
        - work_hours - how many hours you will be working - choices
        - payment_per_hour - decimal field
        - work_permit - choices
        - drivers_license - choices
        - upload_cv - upload file field
    return: TODO
    """

    # Personal Information Fields
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
    mobile_phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format:'+999999999'.\
                Up to 15 digits allowed."
    )
    mobile_phone_number = models.CharField(
        validators=[mobile_phone_regex],
        max_length=15,
        blank=True
    )
    city = models.CharField(
        _("City"),
        max_length=6,
        choices=FIVE_BOROUGH
    )
    street_address = models.CharField(
        _("Street Address"),
        max_length=225,
        blank=True
    )

    # Experience Information fields
    candidate_skill = models.CharField(
        _("Skill"),
        max_length=6,
        choices=SKILL_CHOICE_TYPE
    )
    candidate_experience = models.CharField(
        _("Real Experience"),
        max_length=7,
        choices=EXPERIENCE_CHOICE_TYPE
    )
    candidate_hospitality_experience = models.CharField(
        _("Hospitality Experience"),
        max_length=7,
        choices=EXPERIENCE_CHOICE_TYPE
    )
    candidate_training = models.CharField(
        _("Handyman Training"),
        max_length=4,
        choices=TRAINING_CHOICE_FIELD
    )
    reference_letter = models.FileField(
        _("Reference Letter"),
        upload_to="reference_letter/",
        blank=True
    )

    # Other Informations
    work_hours = models.CharField(
        _("Work Hours"),
        max_length=4,
        choices=WORK_HOURS_CHOICE_FIELD
    )
    payed_per_hour = models.DecimalField(
        _("Timetable"),
        max_digits=2,
        decimal_places=1
    )
    valid_work_permit = models.CharField(
        _("Valid Work Permit"),
        max_length=2,
        choices=WORK_PERMIT_CHOICE_FIELD
    )
    drivers_license = models.CharField(
        _("Driver License"),
        max_length=6,
        choices=DRIVERS_LICENSE_CHOICE_FIELD
    )
    upload_cv = models.FileField(
        _("Upload CV"),
        upload_to="candidate_cv/",
    )

    class Meta:
        verbose_name = _("CandindateForm")
        verbose_name_plural = _("CandindateForms")
        ordering = ("email",)

    def __str__(self):
        return self.email


@python_2_unicode_compatible
class MultilingualModelIdea(models.Model):
    """TODO: Crete MultilingualModelField, this is just a small
    example of what we can do, for future notice we are going to
    extend this model instance.
    MultilingualModelField contains:
        - title - this is related to MultilingualCharField
        - description - this is related to MultilingualTextField

    Both MultilingualCharField and MultilingualTextField are defined in
    utils/fields.py and they are representing django multilingual mechanism
    return: TODO
    """
    title = MultilingualCharField(
        _("Title"),
        max_length=225
    )
    description = MultilingualTextField(
        _("Description"),
        blank=True,
    )

    class Meta:
        verbose_name = _("MultilingualModelIdea")
        verbose_name_plural = _("MultilingualModelIdeas")

    def __str__(self):
        return self.title
