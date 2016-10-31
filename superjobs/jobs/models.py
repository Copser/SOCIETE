from django.db import models

# Create your models here.
class HousekeepAd(models.Model):
    """TODO: init CarpenterAd, we will register this model into Admin
    return: TODO
    """
    housekeep_ad_title = models.CharField(max_length=225)
    houskeep_ad_details = models.TextField()
    houskeep_ad_created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.housekeep_ad_title


class PlumbingAd(models.Model):
    """TODO: init CarpenterAd, we will register this model into Admin
    return: TODO
    """
    plumbing_ad_title = models.CharField(max_length=225)
    plumbing_ad_details = models.TextField()
    plumbing_ad_created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.plumbing_ad_title


class ElectricalAd(models.Model):
    """TODO: init CarpenterAd, we will register this model into Admin
    return: TODO
    """
    electrical_ad_title = models.CharField(max_length=225)
    electrical_ad_details = models.TextField()
    electrical_ad_created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.electrical_ad_title


class ConstructionAd(models.Model):
    """TODO: init CarpenterAd, we will register this model into Admin
    return: TODO
    """
    contruction_ad_title = models.CharField(max_length=225)
    construction_ad_details = models.TextField()
    construction_ad_created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.contruction_ad_title


class HAVCAd(models.Model):
    """TODO: init CarpenterAd, we will register this model into Admin
    return: TODO
    """
    hvac_ad_title = models.CharField(max_length=225)
    hvac_ad_details = models.TextField()
    hvac_ad_created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hvac_ad_title
