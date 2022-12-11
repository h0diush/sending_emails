from .base import *
from .local_settings import LOCAL_DATABASES

LOCAL_APPS = [
    'apps.users.apps.UsersConfig',
    'apps.sending_emails.apps.SendingEmailsConfig'
]

THIRD_PARTY_APPS = [
    'ckeditor',
    'ckeditor_uploader',
    'crispy_forms',
    'registration',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

DEV_DATABASES = {
    'default': {
        'ENGINE': env('DB_ENGINE'),
        'NAME': env('DB_NAME'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT')
    }
}


def _start_db():
    if DEBUG:
        return LOCAL_DATABASES
    return DEV_DATABASES
    # return DEVELOPMENT_DATABASES


DATABASES = _start_db()
