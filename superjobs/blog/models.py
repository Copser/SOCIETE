from django.db import models
from django.contrib.auth.models import User

from uuslug import uuslug
import datetime

# Create your models here.
class Post(models.Model):
    """TODO: Create one model for Jobs representation,
    this models is represented with title, description,
    created_at, tag, views and slug field.
    I'm using standard slug logic to generate valid
    urls.

    This model is extended in serializers and for this
    model we have setup and PostSerializer, I'm adding
    owner for Post so it will be used for django-rest-framework
    authentication and permissions
    return: TODO
    """
    title = models.CharField(
        max_length=225
    )
    description = models.TextField()
    created_at = models.DateTimeField(
        default=datetime.datetime.now
    )
    tag = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )
    views = models.IntegerField(
        default=0
    )
    slug = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = uuslug(
            self.title,
            instance=self,
            max_length=100
    )
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']


class Apply(models.Model):
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

    applicants_timestamp = models.DateTimeField(
        default=datetime.datetime.now
    )

    def __str__(self):
        return self.email

    class Meta:
        ordering = ('applicants_timestamp',)
