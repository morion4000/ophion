from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

from movies.models import Movie


class List(models.Model):
    FAVORITE = 'FAV'
    SEEN = 'SEE'
    MUST_SEE = 'MSE'
    CUSTOM = 'CUS'
    TYPE_CHOICES = (
        (FAVORITE, 'Favorite'),
        (SEEN, 'Seen'),
        (MUST_SEE, 'Must See'),
        (CUSTOM, 'Custom'),
    )

    user = models.ForeignKey(User)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    movies = models.ManyToManyField(Movie, default=None)
    pub_date = models.DateTimeField('date published', default=datetime.now, blank=True)
    privacy = models.BooleanField('private', default=False)
    type = models.CharField(max_length=3,
                            choices=TYPE_CHOICES,
                            default=CUSTOM)

    def __unicode__(self):
        return self.user.username + ' - ' + self.name

    def thumbnail(self):
        movies = self.movies.all()
        movies_len = len(movies)

        if movies_len > 0:
            return movies[movies_len-1].medium_thumbnail()

        return None
