from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from django.shortcuts import render_to_response


urlpatterns = [
    # Examples:
    # url(r'^$', 'societe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # auto-comeplete-light urls

    url(r'^$', 'landing_page.views.index', name='index'),
    url(r'^about/', 'landing_page.views.about', name='about'),

    # check_in
    url(r'^check_in/', include('check_in.urls')),

    # robots.txt
    url(r'^robots.txt$',
        lambda r:
        render_to_response('robots.txt', content_type='text/plain')),

    # allauth urls
    url(r'^accounts/', include('allauth.urls')),
]
