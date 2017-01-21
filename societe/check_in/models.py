# check_in/models.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django_countries.fields import CountryField
import datetime

# Create your models here.
class InitialCharacteristicModel(models.Model):
    """TODO: InitialCharacteristicModels is collecting
    personal data from are user, as if move in and move out
    date.
    Model field for InitialCharacteristicModels are:
        Personal Information:
            - First Name
            - Last Name
            - Email
            - Country
        What do you want to know about the building, house,
        etc:
            - Empty Field (Field Set)

    return: TODO
    """
    #
    # Personal Information
    first_name = models.CharField(_("First Name"), max_length=225, blank=True, null=True)
    last_name = models.CharField(_("Last Name"), max_length=225, blank=True, null=True)
    email = models.EmailField(_("Email"), max_length=225, blank=True, null=True)
    country = CountryField(blank=True, null=True)

    # Residence Information
    your_questions = models.CharField(_("Your Questions"), max_length=300, blank=True, null=True)
    message = models.TextField()

    # Time when this model instance is created
    timestamp = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        verbose_name = _("InitialCharacteristicModel")
        verbose_name_plural = _("InitialCharacteristicModels")
        ordering = ("-timestamp",)

    def __str__(self):
        return self.email
