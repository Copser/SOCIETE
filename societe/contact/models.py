from django.db import models
from django_countries.fields import CountryField
import datetime

# Create your models here.


class ContactForm(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=250)
    mobile = models.CharField(max_length=32, blank=True)
    timestamp = models.DateTimeField(default=datetime.datetime.now)
    birthday = models.DateField(null=True)
    move_in_date = models.DateField(null=True)
    move_out_date = models.DateField(null=True)
    country = CountryField()
    message = models.TextField()

    def __unicode__(self):
        """TODO: Docstring for __unicode__.
        :returns: TODO

        """
        return self.email

    class Meta:
        ordering = ['-timestamp']
