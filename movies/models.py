from datetime import datetime
from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=100)
    thumbnail = models.URLField()
    synopsis = models.TextField()
    release_date = models.CharField(max_length=50)
    tmdb = models.CharField(max_length=50)
    imdb = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published', default=datetime.now, blank=True)

    def __unicode__(self):
        return self.name

    def small_thumbnail(self):
        return 'https://image.tmdb.org/t/p/w92%s' % self.thumbnail

    def medium_thumbnail(self):
        return 'https://image.tmdb.org/t/p/w185%s' % self.thumbnail
