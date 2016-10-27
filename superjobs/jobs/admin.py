from django.contrib import admin
from jobs.models import CarpenterAd, HousekeepAd, PlumbingAd, ElectricalAd, ConstructionAd, HAVCAd

# Register your models here.
class CarpenterAdAdmin(admin.ModelAdmin):
    """TODO: register CarpenterAd model
    return: TODO
    """
    class Meta:
        model = CarpenterAd


class HousekeepAdAdmin(admin.ModelAdmin):
    """TODO: register HousekeepAd
    return: TODO
    """
    class Meta:
        model = HousekeepAd


class PlumbingAdAdmin(admin.ModelAdmin):
    """TODO: register PlumbingAd
    return: TODO
    """
    class Meta:
        model = PlumbingAd


class ElectricalAdAdmin(admin.ModelAdmin):
    """TODO: register ElectricalAd
    return: TODO
    """
    class Meta:
        model = ElectricalAd


class ConstructionAdAdmin(admin.ModelAdmin):
    """TODO: register ConstructionAd
    return: TODO
    """
    class Meta:
        model = ConstructionAd


class HAVCAdAdmin(admin.ModelAdmin):
    """TODO: register HAVCAd
    return: TODO
    """
    class Meta:
        model = HAVCAd

admin.site.register(CarpenterAd, CarpenterAdAdmin)
admin.site.register(HousekeepAd, HousekeepAdAdmin)
admin.site.register(PlumbingAd, PlumbingAdAdmin)
admin.site.register(ElectricalAd, ElectricalAdAdmin)
admin.site.register(ConstructionAd, ConstructionAdAdmin)
admin.site.register(HAVCAd, HAVCAdAdmin)
