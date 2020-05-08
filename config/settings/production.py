"""Production settings"""
from .base import *
from .base import env


# Base
SECRET_KEY = env('DJANGO_SECRET_KEY')
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS',default=['direccion.com'])

# Databases
DATABASES['default'] = env.db('DATABASE_URL')
DATABASES['default']['ATOMIC_REQUESTS'] = True
DATABASES['default']['CONN_MAX_AGE'] = env.int('CONN_MAX_AGE',default=60)

# Caches
CACHES = {
    'default':{
        'BACKEND':'django_redis.cache.RedisCache',
        'LOCATION':env('Redis_URL'),
        'OPTIONS':{
            'CLIENT_CLASS':'django_redis.cache.RedisCache',
            'IGNORE_EXCEPTIONS':True
        }
    }
}

# Security
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO','https')
SECURE_SSL_REDIRECT = env.bool('DJANGO_SECURE_SSL_REDIRECT',default=True)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool('DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS',default=True)
SECURE_HSTS_PRELOAD = env.bool('DJANGO_SECURE_HSTS_PRELOAD',default=True)
SECURE_CONTENT_TYPE_NOSNIFF = env.bool('DJANGO_SECURE_CONTENT_TYPE_NOSNIFF',default=True)

# Storages
INSTALLED_APPS += ['storages']
AWS_ACCES_KEY_ID = env('DJANGO_AWS_ACCES_KEY_ID')
AWS_SECRET_ACCES_KEY = env('DJANGO_AWS_SECRET_ACCES_KEY')
AWS_STORAGE_BUCKET_NAME = env('DJANGO_AWS_STORAGE_BUCKET_NAME')
AWS_QUERYSTRING_AUTH = False
_AWS_EXPIRY = 60 * 60 * 24 * 7
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl':f'max-age={_AWS_EXPIRY},s-maxage = {_AWS_EXPIRY}, must-revalidate',
}

# Static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFileStorage'

# Media
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/'

# Templates
TEMPLATES[0]['OPTIONS']['loaders'] = [
    (
        'django.template.loaders.cached.Loader',
        [
            'django.templates.loaders.filesystem.Loader',
            'django.template.loaders.app_directorios.Loader'
        ]
    ),
]

# Email

DEFAULT_FROM_EMAIL = env(
    'DJANGO_DEFAULT_FROM_EMAIL',
    default = 'comparte aplicacion <noreply@aplicacion.com>'
)
SERVER_MAIL = env('DJANGO_SERVER_EMAIL',default=DEFAULT_FROM_EMAIL)
EMAIL_SUBJECTS_PREFIX = env('DJANGO_EMAIL_SUBJECTS_PREFIX',default='[comparte aplicacion]')

# Admin
ADMIN_URL = env('DJANGO_ADMIN_URL')

# Anymail (mailgun)

INSTALLED_APPS += ['anymail']
EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'

ANYMAIL = {
    'MAILGUN_API_KEY':env('MAILGUN_API_KEY')
    'MAILGUN_SENDER_DOMAIN': env('MAILGUN_DOMAIN')
}

# Gunicorn
INSTALLED_APPS += ['gunicorn']

# Whitenoise
MIDDLEWARE.insert(1,'whitenoise.middleware.WhiteNoiseMiddleware')






