from django.db import models
from django.contrib.auth.models import User

import datetime

# Create your models here.
class Jobs(models.Model):
    """TODO: Create one model for Jobs representation, initiate choice field for are job categories, rest of the fields are simeple title, desctiption and create timestamp firld
    return: TODO
    """
    CARPENTER = 1
    HOUSEKEEP = 2
    PLUMBING = 3
    ELECTRICAL = 4
    CONSTRUCTION = 5
    HVAC = 6
    JOBS_CHOICES = (
        (CARPENTER, 'Carpenter'),
        (HOUSEKEEP, 'Housekeep'),
        (PLUMBING, 'Plumbing'),
        (ELECTRICAL, 'Electrical'),
        (CONSTRUCTION, 'Construction'),
        (HVAC, 'HVAC'),
    )
    title = models.CharField(
        max_length=225
    )
    description = models.TextField()
    categories = models.CharField(
        max_length=1,
        choices=JOBS_CHOICES,
        default=CARPENTER)
    created_at = models.DateTimeField(
        default=datetime.datetime.now
    )

    def __str__(self):
        return self.jobs_advertisment_title

    class Meta:
        ordering = ['-created_at']


class ApplyTo(models.Model):
    """TODO: Define model for future Apply_now form
    return: TODO
    """
    full_name = models.CharField(
        max_length=225
    )
    email = models.EmailField(
        max_length=225
    )
    mobile = models.CharField(
        max_length=225
    )
    birthdate = models.DateField(
        blank=True,
        null=True
    )

    previous_company_name = models.CharField(
        max_length=225
    )
    previous_company_email = models.CharField(
        max_length=225
    )
    previous_job_title = models.CharField(
        max_length=225
    )

    jobs_experience = models.TextField()
    hospitality_relations_experience = models.TextField()

    working_hours = models.CharField(
        max_length=225
    )
    choose_desired_working_hours_wage = models.DecimalField(
        max_digits=2,
        decimal_places=0)

    DRIVERS_CATEGORY_CHOICES = (
        (u'1', u'A'),
        (u'2', u'B'),
        (u'3', u'C'),
        (u'4', u'D'),
        (u'5', u'E'),
        (u'6', u'M'),
    )
    type_of_driver_licences = models.CharField(
        max_length=1,
        choices=DRIVERS_CATEGORY_CHOICES)
    applicants_cv = models.FileField(
        upload_to='CV/'
    )

    applicants_timestamp = models.DateTimeField(
        default=datetime.datetime.now
    )

    def __str__(self):
        return self.email

    class Meta:
        ordering = ('applicants_timestamp',)
