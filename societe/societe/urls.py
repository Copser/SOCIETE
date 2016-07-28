from django.conf.urls import include, url
from django.contrib import admin
from django.shortcuts import render_to_response

from payments import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'societe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # auto-comeplete-light urls
    url(r'^autocomplete/', include('autocomplete_light.urls')),

    url(r'^$', 'landing_page.views.index', name='index'),
    url(r'^about/', 'landing_page.views.about', name='about'),
    url(r'^explore/', 'landing_page.views.explore', name='explore'),
    url(r'^contact/', 'contact.views.contact', name='contact'),
    url(r'^success/', 'contact.views.success', name='success'),

    # robots.txt
    url(r'^robots.txt$',
        lambda r:
        render_to_response('robots.txt', content_type='text/plain')),

    # url(r'^paypal/', include('paypal.standard.ipn.urls')),
    # stripe authentication payment urls
    url(r'^register/', views.register, name='register'),
    url(r'^thank_you/', views.thank_you, name='thank_you'),

    # allauth urls
    # url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/', include('allauth.urls')),
]
