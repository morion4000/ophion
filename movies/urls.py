from django.conf.urls import patterns, url

from movies import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='movies.index'),
    url(r'^(\d+)$', views.detail, name='movies.detail'),
    url(r'^search$', views.search, name='movies.search')
)
