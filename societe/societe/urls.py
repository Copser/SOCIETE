from django.conf.urls import include, url
from django.contrib import admin

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

    # paypal payment notify url
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    # payments urls
    url(r'^charge/', 'payments.views.charge', name='charge'),
    url(r'^thank_you/', 'payments.views.thank_you', name='thank_you'),

    # allauth urls
    # url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/', include('allauth.urls')),
]
