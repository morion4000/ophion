from django.conf.urls import patterns, url

from people import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='people.index'),
    url(r'^(\d+)$', views.detail, name='people.detail')
)
