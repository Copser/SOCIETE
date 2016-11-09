from django.contrib import admin

from .models import Jobs, ApplyToJobs

# Register your models here.
class JobsAdmin(admin.ModelAdmin):
    """TODO: register model into admin with a small customization for the model, we are including
    some fieldsets, so we will separate jobs categories from jobs title, description and created_at field
    return: TODO
    """
    fieldsets = [
        ('Job General Information', {'fields': ['jobs_title',
                                                 'jobs_description',
                                                 'jobs_created_at',],
                                      'classes': ['collapse']}),
        ('Job Lists', {'fields': ['jobs_categories']}),]



class ApplyToJobsAdmin(admin.ModelAdmin):
    """TODO: register apply_to form
    return: TODO
    """
    model = ApplyToJobs


admin.site.register(Jobs, JobsAdmin)
admin.site.register(ApplyToJobs, ApplyToJobsAdmin)
