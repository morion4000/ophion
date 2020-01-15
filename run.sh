export DJANGO_SETTINGS_MODULE="ophion.settings.local"
export NEW_RELIC_CONFIG_FILE="newrelic.ini"
export NEW_RELIC_ENVIRONMENT="development"

cd ophion
python manage.py runserver 0.0.0.0:8000
