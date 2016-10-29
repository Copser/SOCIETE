from django.db import models

# Create your models here.
class CarpenterAd(models.Model):
    """TODO: init CarpenterAd, we will register this model into Admin
    return: TODO
    """
    title = models.CharField(max_length=225)
    details = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class HousekeepAd(models.Model):
    """TODO: init CarpenterAd, we will register this model into Admin
    return: TODO
    """
    pass


class PlumbingAd(models.Model):
    """TODO: init CarpenterAd, we will register this model into Admin
    return: TODO
    """
    pass


class ElectricalAd(models.Model):
    """TODO: init CarpenterAd, we will register this model into Admin
    return: TODO
    """
    pass


class ConstructionAd(models.Model):
    """TODO: init CarpenterAd, we will register this model into Admin
    return: TODO
    """
    pass


class HAVCAd(models.Model):
    """TODO: init CarpenterAd, we will register this model into Admin
    return: TODO
    """
    pass
