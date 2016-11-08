from django.contrib import admin

from .models import Job, ApplyToJob

# Register your models here.
class JobAdmin(admin.ModelAdmin):
    """TODO: register model into admin with a small customization for the model, we are including
    some fieldsets, so we will separate jobs categories from jobs title, description and created_at field
    return: TODO
    """
    fieldsets = [
        ('Job General Information', {'fields': ['job_title',
                                                 'job_description',
                                                 'job_created_at',],
                                      'classes': ['collapse']}),
        ('Job Lists', {'fields': ['job_categories']}),]



class ApplyToJobAdmin(admin.ModelAdmin):
    """TODO: register apply_to form
    return: TODO
    """
    model = ApplyToJob


admin.site.register(Job, JobAdmin)
admin.site.register(ApplyToJob, ApplyToJobAdmin)
