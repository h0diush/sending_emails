from .base import *
from .local_settings import LOCAL_DATABASES

LOCAL_APPS = [
    'apps.users.apps.UsersConfig',
    'apps.sending_emails.apps.SendingEmailsConfig'
]

THIRD_PARTY_APPS = [
    'ckeditor',
    'ckeditor_uploader',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


def _start_db():
    if DEBUG:
        return LOCAL_DATABASES
    # return DEVELOPMENT_DATABASES


if DEBUG:
    DATABASES = _start_db()
