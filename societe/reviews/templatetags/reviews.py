from django import template
from django.conf import settings

register = template.Library()
from reviews.models import OnMapReviewLayout


@register.inclusion_tag("reviews/tags/dummy.html")
def get_map_layout(layout, number=5, template="reviews/tags/_map_layout.html"):
    """doc"""
    return {'template': template,
            'queryset': layout.reviews.all().order_by('-position_y'),
            'MEDIA_URL': settings.MEDIA_URL, }
