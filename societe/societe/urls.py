from django.conf.urls import include, url
from django.contrib import admin
from .payments import views

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
    url(r'^success/', 'contact.views.success', name='success'),

    # allauth urls
    # url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/', include('allauth.urls')),

    # user registration/authentication for payments
    url(r'^sign_in$', views.sign_in, name='sign_in'),
    url(r'^sign_out$', views.sign_out, name='sign_out'),
    url(r'^register$', views.register, name='register'),
    url(r'^edit$', views.edit, name='edit'),

]
