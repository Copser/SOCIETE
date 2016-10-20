from django.contrib import admin
from labor_apply_app.models import PersonalInfo

# Register your models here.
class PersonalInfoAdmin(admin.ModelAdmin):
    """TODO: register PersonalInfo to admin
    return: TODO
    """
    class Meta:
        model = PersonalInfo

admin.site.register(PersonalInfo, PersonalInfoAdmin)
