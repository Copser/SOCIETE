from django.contrib import admin

from .models import Post, Apply

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    """TODO: register model into admin with a small customization for the model, we are including
    some fieldsets, so we will separate jobs categories from jobs title, description and created_at field
    return: TODO
    """
    fieldsets = [
        ('Job General Information',
         {'fields': ['title', 'description', 'tag', 'created_at'],
           'classes': ['collapse']}),
    ]



class ApplyAdmin(admin.ModelAdmin):
    """TODO: register apply_to form
    return: TODO
    """
    model = Apply


admin.site.register(Post, PostAdmin)
admin.site.register(Apply, ApplyAdmin)
