from django.db import models
import datetime

# Create your models here.
#

class SuperReference(models.Model):
    """ return: answers multiple fields """
    company_name = models.CharField(max_length=255)
    company_email = models.EmailField(max_length=255)
    company_phone = models.CharField(max_length=100)
    job_title = models.CharField(max_length=255)


class SuperExperience(models.Model):
    """ renturn: answers to multiple fields """
    work_experience = models.TextField()
    hospitality = models.TextField()


class SuperApplyForm(models.Model):
    """ Create new model for are form, we will extend this using djangorest """
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=100)
    previous_job = models.ForeignKey(
        SuperReference,
        on_delete=models.CASCADE,
    )
    relevante_experience = models.ForeignKey(
        SuperExperience,
        on_delete=models.CASCADE,
    )
    hourly_rate = models.IntegerField()
    working_hours = models.IntegerField()
    drivers_license = models.CharField(max_length=100)
    curriculum_vitae = models.FileField(upload_to='CV')
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        """TODO: Docstring for __unicode__
        returns: TODO
        """
        return self.email

    class Meta:
        """TODO: Docstring for __unicode__
        returns: TODO
        """
        ordering = ('created',)
