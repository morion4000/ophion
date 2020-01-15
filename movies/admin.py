from django.contrib import admin

from movies.models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date', 'tmdb', 'imdb')
    search_fields = ('name', 'imdb', 'tmdb')

admin.site.register(Movie, MovieAdmin)
