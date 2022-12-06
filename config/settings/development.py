from .base import *
from .local_settings import LOCAL_DATABASES

LOCAL_APPS = [
    'apps.users',
    'apps.sending_emails'
]

THIRD_PARTY_APPS = []

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

if DEBUG:
    DATABASES = LOCAL_DATABASES
