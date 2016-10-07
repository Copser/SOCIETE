from django.db import models
# from django.forms import ModelForm
import datetime

# Create your models here.
DRIVERS_CATEGORY_CHOICES = (
    ('A', 'B'),
    ('C', 'D'),
    ('E', 'None'),
)


class LaborInfo(models.Model):
    """TODO: Model for Labor Users
    return: TODO
    """
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    mobile = models.CharField(max_length=100)
    birthdate = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.full_name


class LaborReference(models.Model):
    """TODO:
    return: TODO
    """
    labor_info = models.ForeignKey(LaborInfo, null=False, blank=True)
    company_name = models.CharField(max_length=255)
    company_email = models.EmailField(max_length=255)
    company_phone = models.CharField(max_length=100)
    previous_job_title = models.CharField(max_length=255)


class LaborExperience(models.Model):
    """TODO:
    return: TODO
    """
    labor_info = models.ForeignKey(LaborInfo, null=False, blank=True)
    relevante_experience = models.TextField()
    hospitality = models.TextField()

class FutureLaborInfo(models.Model):
    """TODO:
    return: TODO
    """
    labor_info = models.ForeignKey(LaborInfo, null=False, blank=True)
    future_working_hourse = models.CharField(max_length=255)
    hourly_rate = models.DecimalField(max_digits=4, decimal_places=2)
    drivers_license = models.CharField(max_length=6, choices=DRIVERS_CATEGORY_CHOICES)
    curriculum_vitae = models.FileField(upload_to='cv/')
