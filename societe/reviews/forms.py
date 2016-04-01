import autocomplete_light
autocomplete_light.autodiscover()

from reviews.models import OnMapReviewLayout


class OnMapReviewLayoutForm(autocomplete_light.ModelForm):
    class Meta:
        model = OnMapReviewLayout
        autocomplete_names = {'reviews': 'OnMapReviewAutocomplete', }
        autocomplete_fields = ('reviews',)
        fields = "__all__"
