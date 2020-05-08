from .base import *
from .base import env

# Base
DEBUG = True

# Security
SECRET_KEY = env('DJANGO_SECRET_KEY',default='1xrfy57r1y&yia1#h5!k%a$juo(5bhp68is))(+=1)7443wbfa')
ALLOWED_HOSTS = [
    'localhost',
    '0.0.0.0',
    '127.0.0.1',
]

# Cache
CACHES = {
    'default':{
        'BACKEND':'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION':''
    }
}

# Templates
TEMPLATE[0]['OPTIONS']['debug'] = DEBUG #NOQA

# Email
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',default='django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

# Django-extensions
INSTALLED_APPS += ['django_extensions'] #NOQA F405

# Celery