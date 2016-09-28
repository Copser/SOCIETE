from django.db import models
import datetime

# Create your models here.
#

class Reference(models.Model):
    """TODO: answers multiple fields,
    return: TODO
    """
    company_name = models.CharField(max_length=255)
    company_email = models.EmailField(max_length=255)
    company_phone = models.CharField(max_length=100)
    job_title = models.CharField(max_length=255)


class Experience(models.Model):
    """TODO: answers to multiple fields,
    return: TODO
    """
    work_experience = models.TextField()
    hospitality = models.TextField()


class ApplyForm(models.Model):
    """TODO: Create new model for are form, we will extend this using djangorest,
    return: TODO
    """
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=100)
    previous_job = models.ForeignKey(
        Reference,
        null=False,
        on_delete=models.CASCADE,
    )
    relevante_experience = models.ForeignKey(
        Experience,
        null=False,
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
