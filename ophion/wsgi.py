import os
import newrelic.agent

from dj_static import Cling
from django.core.wsgi import get_wsgi_application

application = Cling(get_wsgi_application())

config_file = os.environ.get('NEW_RELIC_CONFIG_FILE')
environment = os.environ.get('NEW_RELIC_ENVIRONMENT')

newrelic.agent.initialize(config_file, environment)

application = newrelic.agent.WSGIApplicationWrapper(application)