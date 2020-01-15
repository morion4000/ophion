from base import *

DEBUG = False

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

STATIC_ROOT = os.path.join(
	os.path.dirname(
 		os.path.dirname(
			os.path.abspath(__file__))), 'static')

if 'RDS_DB_NAME' in os.environ:
	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.postgresql_psycopg2',
			'NAME': os.environ['RDS_DB_NAME'],
			'USER': os.environ['RDS_USERNAME'],
			'PASSWORD': os.environ['RDS_PASSWORD'],
			'HOST': os.environ['RDS_HOSTNAME'],
			'PORT': os.environ['RDS_PORT'],
	    }
	}
else:
	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.postgresql_psycopg2',
			'NAME': 'ebdb',
			'USER': 'ophion',
			'PASSWORD': 'ophion',
			'HOST': 'ophion.us-west-2.rds.amazonaws.com',
			'PORT': 5432,
	    }
	}

# Get rid of query strings that are added to static resources paths
AWS_QUERYSTRING_AUTH = False

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = 'ophion'
AWS_SECRET_ACCESS_KEY = 'ophion'
AWS_STORAGE_BUCKET_NAME = 'ophion'

BROKER_TRANSPORT = 'sqs'
BROKER_TRANSPORT_OPTIONS = {
    'region': 'us-west-2',
}
BROKER_USER = AWS_ACCESS_KEY_ID
BROKER_PASSWORD = AWS_SECRET_ACCESS_KEY

CELERY_DEFAULT_QUEUE = 'ophion'
CELERY_QUEUES = {
    CELERY_DEFAULT_QUEUE: {
        'exchange': CELERY_DEFAULT_QUEUE,
        'binding_key': CELERY_DEFAULT_QUEUE,
    }
}
