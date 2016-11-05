from django.db import models
from django.contrib.auth.models import User

import datetime

# Create your models here.
class JobsAdvertisment(models.Model):
    """TODO: Create one model for Jobs representation, initiate choice field for are job categories, rest of the fields are simeple title, desctiption and create timestamp firld
    return: TODO
    """
    jobs_advertisment_title = models.CharField(max_length=225)
    jobs_advertisment_desctiption = models.TextField()
    SELECT_THE_DESIRED_JOB_CATEGORY = (
        (u'1', u'Carpenter'),
        (u'2', u'Housekepp'),
        (u'3', u'Plumbing'),
        (u'4', u'Electrical'),
        (u'5', u'Construction'),
        (u'6', u'HVAC'),
    )
    jobs_categories = models.CharField(max_length=1, choices=SELECT_THE_DESIRED_JOB_CATEGORY)
    jobs_advertisment_created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.jobs_advertisment_title

    class Meta:
        ordering = ['-jobs_advertisment_created_at']


class JobsApplyTo(models.Model):
    """TODO: Define model for future Apply_now form
    return: TODO
    """
    full_name = models.CharField(max_length=225)
    email = models.EmailField(max_length=225)
    mobile = models.CharField(max_length=225)
    birthdate = models.DateField(blank=True, null=True)

    previous_company_name = models.CharField(max_length=225)
    previous_company_email = models.CharField(max_length=225)
    previous_job_title = models.CharField(max_length=225)

    jobs_experience = models.TextField()
    hospitality_relations_experience = models.TextField()

    working_hours = models.CharField(max_length=225)
    choose_desired_working_hours_wage = models.DecimalField(max_digits=2, decimal_places=0)

    DRIVERS_CATEGORY_CHOICES = (
        (u'1', u'A'),
        (u'2', u'B'),
        (u'3', u'C'),
        (u'4', u'D'),
        (u'5', u'E'),
        (u'6', u'M'),
    )
    type_of_driver_licences = models.CharField(max_length=1, choices=DRIVERS_CATEGORY_CHOICES)
    applicants_cv = models.FileField(upload_to='CV/')

    applicants_timestamp = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ('applicants_timestamp',)
