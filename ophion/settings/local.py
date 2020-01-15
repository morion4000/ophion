from base import *

DEBUG = True

TEMPLATE_DEBUG = DEBUG

INTERNAL_IPS = ('10.0.2.2', '0.0.0.0', '127.0.0.1', '::1',)

DEBUG_TOOLBAR_PATCH_SETTINGS = False 

INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ophion',                      
        'USER': 'ophion',
        'PASSWORD': 'ophion',
        'HOST': 'localhost'
    }
}

BROKER_URL = 'amqp://ophion:ophion@localhost:5672//'