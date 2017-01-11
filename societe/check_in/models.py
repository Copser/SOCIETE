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
            - Birthday
            - Country
        Residence Information:
            - Move in Date
            - Move out Date
            - Message

    return: TODO
    """
    #
    # Personal Information
    first_name = models.CharField(
        _("First Name"),
        max_length=225
    )
    last_name = models.CharField(
        _("Last Name"),
        max_length=225
    )
    email = models.EmailField(
        _("Email"),
        max_length=225
    )
    birthday = models.DateField(
        _("Birthday"),
        null=True
    )
    country = CountryField()

    # Residence Information
    move_in_date = models.DateField(
        _("Move in date"),
        null=True
    )
    move_out_date = models.DateField(
        _("Move out date"),
        null=True
    )
    message = models.TextField()

    # Time when this model instance is created
    timestamp = models.DateTimeField(
        default=datetime.datetime.now
    )

    class Meta:
        verbose_name = _("InitialCharacteristicModel")
        verbose_name_plural = _("InitialCharacteristicModels")
        ordering = ("-timestamp",)

    def __str__(self):
        return self.email
