from django.conf.urls import patterns, url

from lists import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='lists.index'),
    url(r'^(\d+)$', views.detail, name='lists.detail'),
    url(r'^add$', views.add, name='lists.add'),
    url(r'^delete/(\d+)$', views.delete, name='lists.delete'),
    url(r'^add_movie$', views.add_movie, name='lists.add_movie'),
    url(r'^import_list/(\d+)$', views.import_list, name='lists.import_list'),
    url(r'^change_privacy/(\w+)/(\d+)$', views.change_privacy, name='lists.change_privacy')
)
