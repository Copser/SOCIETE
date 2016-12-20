# blog/models.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User

from uuslug import uuslug
import datetime

from utils.choices import FIVE_BOROUGH, SKILL_CHOICE_TYPE, \
        TRAINING_CHOICE_FIELD, EXPERIENCE_CHOICE_TYPE, \
        WORK_HOURS_CHOICE_FIELD, WORK_PERMIT_CHOICE_FIELD, \
        DRIVERS_LICENSE_CHOICE_FIELD
from utils.fields import MultilingualCharField, \
        MultilingualTextField


# Create your models here.
@python_2_unicode_compatible
class Post(models.Model):
    """TODO: Create one model for Jobs representation,
    this models is represented with title, description,
    created_at, tag, views and slug field.
    I'm using standard slug logic to generate valid
    urls.

    This model is extended in serializers and for this
    model we have setup and PostSerializer, I'm adding
    owner for Post so it will be used for django-rest-framework
    authentication and permissions
    return: TODO
    """
    title = models.CharField(
        max_length=225
    )
    description = models.TextField()
    created_at = models.DateTimeField(
        default=timezone.now
    )
    tag = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )
    views = models.IntegerField(
        default=0
    )
    slug = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = uuslug(
            self.title,
            instance=self,
            max_length=100
    )
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']


# Create your models here.
@python_2_unicode_compatible
class ApplyFormModel(models.Model):
    """TODO: Define Candidate model for future Candindate Form, this model
    is deffined of three part's Personal Information, Experience Information
    and Additional Information.
    This code will be reusable with python 2, choices fields will be added from
    choices.py

    In Personal Information we will make:
        - first_name - char field
        - last name - char field
        - email - email field
        - mobile phone - integer field
        - confirm mobile phone - we will use twillio
        - city - Once city for the beginning New York City
                but I will add choice field about which part
                of the NYC do you live?
                choices
        - street address - char field

    Experience Information will contain:
        - candidate_skill - choices
        - candidate_experience -  choices
        - candidate_hospitality_experience - choices
        - candidate_training - choices

    Other Information will contain:
        - work_hours - choices
        - payment_per_hour - decimal field
        - valid_work_permit - choices
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
    )
    mobile_phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format:'+999999999'.\
                Up to 15 digits allowed."
    )
    mobile_phone = models.CharField(
        validators=[mobile_phone_regex],
        max_length=100,
    )
    confirm_mobile_phone = models.CharField(
        validators=[mobile_phone_regex],
        max_length=100,
    )
    city = models.CharField(
        _("City"),
        max_length=100,
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
        max_length=100,
        choices=SKILL_CHOICE_TYPE
    )
    candidate_experience = models.CharField(
        _("Real Experience"),
        max_length=100,
        choices=EXPERIENCE_CHOICE_TYPE
    )
    candidate_hospitality_experience = models.CharField(
        _("Hospitality Experience"),
        max_length=100,
        choices=EXPERIENCE_CHOICE_TYPE
    )
    candidate_training = models.CharField(
        _("Handyman Training"),
        max_length=100,
        choices=TRAINING_CHOICE_FIELD
    )

    # Other Informations
    work_hours = models.CharField(
        _("Work Hours"),
        max_length=100,
        choices=WORK_HOURS_CHOICE_FIELD
    )
    payed_per_hour = models.DecimalField(
        _("Timetable"),
        max_digits=11,
        decimal_places=2,
        null=True
    )
    valid_work_permit = models.CharField(
        _("Valid Work Permit"),
        max_length=100,
        choices=WORK_PERMIT_CHOICE_FIELD
    )
    drivers_license = models.CharField(
        _("Driver License"),
        max_length=100,
        choices=DRIVERS_LICENSE_CHOICE_FIELD
    )
    upload_cv = models.FileField(
        _("Upload CV"),
        upload_to="candidate_cv/",
    )
    created_at = models.DateTimeField(
        default=datetime.datetime.now
    )

    class Meta:
        verbose_name = _("CandindateForm")
        verbose_name_plural = _("CandindateForms")
        ordering = ("-created_at",)

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
