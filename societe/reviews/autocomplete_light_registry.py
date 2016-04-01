import autocomplete_light.shortcuts as al

from reviews.models import OnMapReview

# This will generate a OnMapReviewAutocomplete class
al.register(OnMapReview,
            search_fields=['^id', 'name'],
            attrs={'placeholder': 'Name or ID',
                   'data-autocomplete-minimum-characters': 1, },
            widget_attrs={'data-widget-maximum-values': 16, },
            )
