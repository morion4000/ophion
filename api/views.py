from tmdbsimple import TMDB

from django.shortcuts import render
from django.conf import settings


def search(request, query):
    tmdb = TMDB(settings.TMDB_API_KEY)
    search = tmdb.Search()
    response = search.movie({
        'query': query,
        'page': 1,
        'search_type': 'ngram'
    })

    for result in search.results:
        result['tokens'] = result['title'].split(' ')

    return render(request, 'api/search.json', {
        'results': search.results
    }, content_type='application/json')
