# Imports

import environ

env = environ.Env()

# Settings

SECRET_KEY = env('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'HOST': env('POSTGRES_HOST'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'PORT': 5432,
    }
}

# Google

GOOGLE_API_KEY = env('GOOGLE_API_KEY')

# Stripe

STRIPE_LIVE_MODE = False

# Rest Framework

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('knox.auth.TokenAuthentication',),
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.JSONRenderer',
    )
}