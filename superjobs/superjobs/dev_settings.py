from .settings import *



# Heroku Configurations
# Parse database configuration from $DATABASE_URL
import dj_database_url

DATABASES = {'default': dj_database_url.config()}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# loading local_settings.py
try:
    from .local_settings import *
except Exception as e:
    pass

# ALLAUTH configuration


# Specific the login method to use
ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_AUTHENTICATION_METHOD = "username", "email", "username_email"

# Determines the e-mail verification method during signup – choose one of “mandatory”, “optional”, or “none”.
# When set to “mandatory” the user is blocked from logging in until the email address is verified.
# Choose “optional” or “none” to allow logins with an unverified e-mail address.
# In case of “optional”, the e-mail verification mail is still sent,
# whereas in case of “none” no e-mail verification mails are sent.
ACCOUNT_EMAIL_VERIFICATION = "none"

# Determines whether or not the user is automatically logged out by a mere GET request.
# See documentation for the LogoutView for details.
ACCOUNT_LOGOUT_ON_GET = False

# Request e-mail address from 3rd import party account provider?
# E.g. using OpenID AX, or the Facebook “email” permission.
SOCIALACCOUNT_QUERY_EMAIL = True

# Dictionary containing provider specific settings.
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        # we use facebook js_sdk instead od oauth2
        'METHOD': 'js_sdk',
        'SCOPE': ['email', 'public_profile', 'user_friends'],
        # using AUTH_PARAMS to pass along other parametees
        # to the FB.login JS SDK call
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        # field are fetch from the import Graph API
        'FIELDS': ['first_name', 'last_name', 'email', 'birthday'],
        # JS SDK return a short-lived token suitable for client-side use.
        'EXCHANGE_TOKEN': True,
        # Chose the current active language of the request
        'LOCALE_FUNC': 'path.to.callable',
        'VERIFIED_EMAIL': False,
        # Facebook Graph API version
        'VERSION': 'v2.7'
    },
    'linkedin': {
        'SCOPE': ['r_emailaddress'],
        'PROFILE_FIELDS': [
            'id',
            'first-name',
            'last-name',
            'email-address',
            'public-profile-url'
        ]
    }
}

# login redirect url
LOGIN_REDIRECT_URL = "/blog/jobs"

# Default settings
BOOTSTRAP3 = {

    # The URL to the jQuery JavaScript file
    'jquery_url': '//code.jquery.com/jquery.min.js',

    # The Bootstrap base URL
    'base_url': '//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/',

    # The complete URL to the Bootstrap CSS file (None means derive it from base_url)
    'css_url': None,

    # The complete URL to the Bootstrap CSS file (None means no theme)
    'theme_url': None,

    # The complete URL to the Bootstrap JavaScript file (None means derive it from base_url)
    'javascript_url': None,

    # Put JavaScript in the HEAD section of the HTML document (only relevant if you use bootstrap3.html)
    'javascript_in_head': False,

    # Include jQuery with Bootstrap JavaScript (affects django-bootstrap3 template tags)
    'include_jquery': False,

    # Label class to use in horizontal forms
    'horizontal_label_class': 'col-md-3',

    # Field class to use in horizontal forms
    'horizontal_field_class': 'col-md-9',

    # Set HTML required attribute on required fields
    'set_required': True,

    # Set HTML disabled attribute on disabled fields
    'set_disabled': False,

    # Set placeholder attributes to label if no placeholder is provided
    'set_placeholder': True,

    # Class to indicate required (better to set this in your Django form)
    'required_css_class': '',

    # Class to indicate error (better to set this in your Django form)
    'error_css_class': 'has-error',

    # Class to indicate success, meaning the field has valid input (better to set this in your Django form)
    'success_css_class': 'has-success',

    # Renderers (only set these if you have studied the source and understand the inner workings)
    'formset_renderers':{
        'default': 'bootstrap3.renderers.FormsetRenderer',
    },
    'form_renderers': {
        'default': 'bootstrap3.renderers.FormRenderer',
    },
    'field_renderers': {
        'default': 'bootstrap3.renderers.FieldRenderer',
        'inline': 'bootstrap3.renderers.InlineFieldRenderer',
    },
}
