from django.db import models
import datetime

# Create your models here.
DRIVERS_CATEGORY_CHOICES = (
    ('A', 'B'),
    ('C', 'D'),
    ('E', 'None'),
)


class PersonalInfo(models.Model):
    """TODO: Write are Labor model to extend in serializer
    return: TODO
    """
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    mobile = models.CharField(max_length=255)
    birthdate = models.DateField(blank=True, null=True)

    previous_company_name = models.CharField(max_length=255)
    previous_company_email = models.CharField(max_length=255)
    previous_company_phone = models.CharField(max_length=255)
    previous_job_title = models.CharField(max_length=255)

    relevante_experience = models.TextField()
    hospitality_experience = models.TextField()

    future_working_hours = models.CharField(max_length=225)
    hourly_wage = models.DecimalField(max_digits=2, decimal_places=2)
    driver_license = models.CharField(max_length=10, choices=DRIVERS_CATEGORY_CHOICES)
    curriculum_vitae = models.FileField(upload_to='cv/')
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.email

    class Meta:
        ordering = ('created',)
