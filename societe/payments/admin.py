from django.contrib import admin
from .models import User
# Register your models here.


class StripeUserAdmin(admin.ModelAdmin):

    """Docstring for PaymentUserAdmin. """
    class Meta:
        """TODO: to be defined1. """
        model = User

admin.site.register(User, StripeUserAdmin)
