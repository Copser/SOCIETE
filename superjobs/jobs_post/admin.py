from django.contrib import admin

from .models import JobsAdvertisment, JobsApplyTo


# Register your models here.
class JobsAdvertismentAdmin(admin.ModelAdmin):
    """TODO: registering JobsAdvertisment into admin, we will customize it so we can see all job posts by chosing one of several job categories.
    Further more we need to assing apply_now form to each job categorie so we can see all of superjobs applicants for each job.
    return: TODO
    """
    fieldsets = [
        ('Jobs General Information', {'fields': ['jobs_advertisment_title',
                                                 'jobs_advertisment_description',
                                                 'jobs_advertisment_created_at',],
                                      'classes': ['collapse']}),
        ('Jobs Lists', {'fields': ['jobs_categories']}),]


class JobsApplyToAdmin(admin.ModelAdmin):
    """TODO:
    return: TODO
    """
    model = JobsApplyTo


admin.site.register(JobsAdvertisment, JobsAdvertismentAdmin)
admin.site.register(JobsApplyTo, JobsApplyToAdmin)
