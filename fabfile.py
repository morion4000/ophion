# apt-get update
# apt-get upgrade
# apt-get install python-dev
# apt-get install python-pip
# apt-get install libpq-dev # postgres
# apt-get install rabbitmq-server
# pip install -r requirements.txt
 
from fabric.api import *
from fabtools.vagrant import vagrant


@task
def deploy_heroku():
	local('heroku maintenance:on')
	local('git push heroku master')
	local('heroku maintenance:off')


@task
def deploy_aws():
	local('find . -name "*.pyc" -exec rm -rf {} \;')
	local('if [ -f ophion.zip ]; then unlink ophion.zip; fi')
	local('zip ophion.zip -r * .ebextensions')
	local('mv ophion.zip ..')


@task
def hello():
	run('uname')