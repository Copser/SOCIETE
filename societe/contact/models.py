# contact/models.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django_countries.fields import CountryField
import datetime

# Create your models here.


class ContactForm(models.Model):
    first_name = models.CharField(
        _("First Name"),
        max_length=150
    )
    last_name = models.CharField(
        _("Last Name"),
        max_length=150
    )
    email = models.EmailField(
        _("Email"),
        max_length=250
    )
    mobile = models.CharField(
        _("Mobile Phone"),
        max_length=32,
        blank=True
    )
    timestamp = models.DateTimeField(
        default=datetime.datetime.now
    )
    birthday = models.DateField(
        _("Birthday"),
        null=True
    )
    move_in_date = models.DateField(
        _("Move in date"),
        null=True
    )
    move_out_date = models.DateField(
        _("Move out date"),
        null=True
    )
    country = CountryField()
    message = models.TextField()


    class Meta:
        verbose_name = _("ContactForm")
        verbose_name_plural = _("ContactForms")
        ordering = ('-timestamp',)

    def __str__(self):
        return self.email
