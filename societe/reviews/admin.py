from django.contrib import admin

from reviews.models import OnMapReview, OnMapReviewLayout, ReviewCategory
from reviews.forms import OnMapReviewLayoutForm


# Register your models here.
class ReviewCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'codename')
    fields = ('name', 'codename', 'description')
    search_fields = ('name',)


class OnMapReviewInline(admin.StackedInline):
    model = OnMapReviewLayout.reviews.through
    extra = 0
    show_change_link = True


class OnMapReviewAdmin(admin.ModelAdmin):
    inlines = [OnMapReviewInline]
    readonly_fields = ('date_added',)
    list_display = ('id', 'category', 'message', 'date_added')
    fields = ('name', 'photo', 'url', 'category', 'message', ('position_x', 'position_y'), 'date_added')
    list_filter = ('category', 'date_added')


class OnMapReviewLayoutAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')
    fields = ('category', 'reviews')
    list_filter = ('category',)
    form = OnMapReviewLayoutForm

    def change_view(self, request, object_id, extra_context=None):
        """doc"""
        if request.method == 'POST':
            rl = OnMapReviewLayout.objects.get(id=object_id)
            for r in rl.reviews.all():
                position_x = int(request.POST.get('x_review_%s' % r.id, r.position_x))
                position_y = int(request.POST.get('y_review_%s' % r.id, r.position_y))
                if position_x != r.position_x or position_y != r.position_y:
                    r.position_x = position_x
                    r.position_y = position_y
                    r.save(update_fields=['position_x', 'position_y'])

        return super(OnMapReviewLayoutAdmin, self).change_view(
            request, object_id, extra_context=extra_context)

admin.site.register(ReviewCategory, ReviewCategoryAdmin)
admin.site.register(OnMapReview, OnMapReviewAdmin)
admin.site.register(OnMapReviewLayout, OnMapReviewLayoutAdmin)
