from django.conf.urls import include, url
from django.contrib import admin

from payments.views import StripePaymentsView, SuccessView


urlpatterns = [
    # Examples:
    # url(r'^$', 'societe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # auto-comeplete-light urls
    url(r'^autocomplete/', include('autocomplete_light.urls')),

    url(r'^$', 'landing_page.views.index', name='index'),
    url(r'^about/', 'landing_page.views.about', name='about'),
    url(r'^appartments/', 'landing_page.views.appartments', name='appartments'),
    url(r'^contact/', 'contact.views.contact', name='contact'),

    # payments url
    url(r'^subscribe/$', StripePaymentsView.as_view(), name='subscribe'),
    url(r'^thank_you/$', SuccessView.as_view(), name='thank_you'),

    # allauth urls
    # url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/', include('allauth.urls')),
]
