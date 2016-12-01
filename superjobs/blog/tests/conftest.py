import os
import django
from django.conf import settings


# We manually designate which settings we will be using in an evnironment variable
# This is similar what occurs in the "manage.py"
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'superjobs.config.settings')

# pytest automatically calls this function once when tests are run
def pytest_configure():
    settings.DEBUG = False
    # declare any test specific settings, here
    # e.g.
    # settings.PASSWORD_HASHERS = (
    #     'django.contrib.auth.hashers.MD5PasswordHasher',
    # )
    django.setup()
    # Note: in Django =< 1.6 you'll need to run this instead
    # settings.configure()
