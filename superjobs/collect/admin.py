from django.contrib import admin
from .models import ApplySuperForm

# Register your models here.
class ApplySuperFormAdmin(admin.ModelAdmin):
    """
    TODO: register are model, form into admin

    """
    class Meta:
        model = ApplySuperForm

admin.site.register(ApplySuperForm, ApplySuperFormAdmin)
