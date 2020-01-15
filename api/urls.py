from django.conf.urls import patterns, url

from api import views

urlpatterns = patterns('',
    url(r'^search/([a-zA-Z0-9"-% ]+)$', views.search, name='api.search')
)
