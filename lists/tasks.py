from __future__ import absolute_import

from celery.task import group, task

from django.conf import settings

from tmdbsimple import TMDB

from movies.models import Movie
from lists.models import List


@task(ignore_result=True)
def add_movie_to_list(title, list_id):
	tmdb = TMDB(settings.TMDB_API_KEY)

	search = tmdb.Search()
	response = search.movie({'query': title})

	movie_id = 0

	for s in search.results:
		movie_id = s['id']

		break

	movie = tmdb.Movies(movie_id).info()

	new_movie, created = Movie.objects.get_or_create(
		name=movie['title'],
		thumbnail=movie['poster_path'],
		synopsis=movie['overview'],
		release_date=movie['release_date'],
		tmdb=movie['id'],
		imdb=movie['imdb_id']
	)

	current_list = List.objects.get(id=list_id)
	current_list.movies.add(new_movie)

	return created


@task(ignore_result=True)
def import_imdb_list(titles, list_id):
	return group(add_movie_to_list.subtask((title, list_id)) for title in titles).apply_async()
