from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class User(AbstractBaseUser):

    """Docstring for User.Setup model for a User which will enable him different payment options.
        Stripe, Paypal, Skrill, using Visa, Mastercard, etc.
    """
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    # pass field defined in base class
    last_4_digits = models.CharField(max_length=4, blank=True, null=True)
    stripe_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    def __str__(self):
        """TODO: to be defined1. """
        return self.email
