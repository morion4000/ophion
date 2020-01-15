export DJANGO_SETTINGS_MODULE="ophion.settings.local"

cd ophion
celery -A ophion worker -l info
