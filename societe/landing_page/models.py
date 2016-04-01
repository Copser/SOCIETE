from django.db import models
# import datetime


class ContactUsForm(models.Model):

    """Docstring for ContactUsForm. This model is for a small form in AboutUS page """
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=250)
    phone_number = models.CharField(max_length=32, blank=True)
    message = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """TODO: to be defined1. """
        return self.email

    class Meta:
        ordering = ['-timestamp']
