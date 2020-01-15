from django.contrib.sites.models import Site

if Site.objects.count() == 0:
	Site.objects.create(pk=1, domain='ophion.com', name='ophion')