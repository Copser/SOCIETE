from django.db import models
import datetime

# Create your models here.

class ApplySuperForm(models.Model):
    """ Create model for User to apply to SuperJobs """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    telephone = models.CharField(max_length=250, blank=True)
    mobile = models.CharField(max_length=250)
    experience = models.TextField()
    references = models.TextField()
    hourly_rate = models.CharField(max_length=100)
    licences = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        """TODO: Docstring for __unicode__
        returns: TODO
        """
        return self.email

    class Meta:
        """ return timestamp """
        ordering = ('created',)
