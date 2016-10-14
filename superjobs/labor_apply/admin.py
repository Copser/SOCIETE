from django.contrib import admin
from labor_apply.models import LaborInfo

# Register your models here.
class LaborInfoAdmin(admin.ModelAdmin):
    """TODO: add are form to Admin
    return: TODO
    """
    class Meta:
        model = LaborInfo

admin.site.register(LaborInfo, LaborInfoAdmin)
