from django.conf import settings
from django.conf.urls import patterns, include, url
from registration.backends.simple.views import RegistrationView

from django.contrib import admin
admin.autodiscover()


class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return '/'


urlpatterns = patterns('',
    url(r'^$', include('home.urls')),
    url(r'^movies/', include('movies.urls')),
    url(r'^people/', include('people.urls')),
    url(r'^lists/', include('lists.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^accounts/register', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})
)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
