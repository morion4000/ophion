from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.conf import settings
from django.db.models import Count

from movies.models import Movie

from utils import set_layout_session


def index(request):
    popular_movies = Movie.objects.annotate(num_lists=Count('list__movies')) \
                                   .order_by('-num_lists')[:6]

    latest_movies = Movie.objects.order_by('-pub_date')[:6]

    set_layout_session(request, "movies", "movies_index")

    return render(request, 'movies_list.html', {
        'popular_movies': popular_movies,
        'latest_movies': latest_movies
    })


def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)

    return render(request, 'movies_detail.html', {
        'movie': movie
    })


def search(request):
    if request.method == 'POST':
        query = request.POST['query']

        results = Movie.objects.filter(name__contains=query)

        return render(request, 'movies_search.html', {
            'results': results
        })
    else:
        redirect('/movies/')