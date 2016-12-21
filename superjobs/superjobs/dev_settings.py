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

# Axes Configurations
# Number of login attempts allowed before a record is created for the failed logins.
AXES_LOGIN_FAILURE_LIMIT = 3

# After the number os allowed login attempts are exceeded, should we lock this IP (and optinal user agend)?
AXES_LOCK_OUT_AT_FAILURE = True

# If True, lock out / log based on an IP address AND a user agent. This means requests from different import user
# agents but from the import same IP are treated differently.
AXES_USE_USER_AGENT = True

# Defines a period of inactivity after which old failed login attempts will be forgotten. You can set to a
# python timedelta object or an integer, if you set it to be integer it will represent a number of hours
AXES_COOLOFF_TIME = 50

# Specifies a logging mechanism for axes to use
AXES_LOCKOUT_TEMPLATE = 'axes.watch_login'

# Specifies a template to render when a user is locked out. Template receives cooloff_time and failure_limit as
# context variables
AXES_LOCKOUT_TEMPLATE = None

# Specifies a URL to redirect to on lockout. If both AXES_LOCKOUT_TEMPLATE and AXES_LOCKOUT_URL are set, the template
# will be used
AXES_LOCKOUT_URL = None

# If Truem you'll see slightly more logging for Axes
AXES_VERBOSE = True

# The name of the for field that contains your usernames
# AXES_USERNAME_FORM_FIELD = username

# If True prevents to login from IP import under particular user if attempts limit exceed, otherwise lock out based on
# IP. Default: False
AXES_LOCK_OUT_BY_COMBINATION_USER_AND_IP = False

# Crispy forms will use BOOTSTRAP3 TEMPLATE PACK
CRISPY_TEMPLATE_PACK = "bootstrap3"

# MAMCACHE Heroku Configuration
os.environ['MEMCACHE_SERVERS'] = os.environ.get('MEMCACHIER_SERVERS', '').replace(',', ';')
os.environ['MEMCACHE_USERNAME'] = os.environ.get('MEMCACHIER_USERNAME', '')
os.environ['MEMCACHE_PASSWORD'] = os.environ.get('MEMCACHIER_PASSWORD', '')

CACHES = {
    'default': {
        # Use pylibmc
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',

        # Use binary memcache protocol (needed for authentication)
        'BINARY': True,

        # TIMEOUT is not the connection timeout! It's the default expiration
        # timeout that should be applied to keys! Setting it to `None`
        # disables expiration.
        'TIMEOUT': None,

        'OPTIONS': {
            # Enable faster IO
            'tcp_nodelay': True,

            # Keep connection alive
            'tcp_keepalive': True,

            # Timeout settings
            'connect_timeout': 2000, # ms
            'send_timeout': 750 * 1000, # us
            'receive_timeout': 750 * 1000, # us
            '_poll_timeout': 2000, # ms

            # Better failover
            'ketama': True,
            'remove_failed': 1,
            'retry_timeout': 2,
            'dead_timeout': 30,
        }
    }
}
