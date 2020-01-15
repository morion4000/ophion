from tmdbsimple import TMDB

from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from lists.models import List
from lists.forms import ListForm
from lists.tasks import import_imdb_list
from movies.models import Movie

from utils import set_layout_session, parse_csv_file


def index(request):
    popular_lists = List.objects.filter(privacy=False) \
                                .annotate(num_movies=Count('movies')) \
                                .order_by('-num_movies')[:6]

    latest_lists = List.objects.filter(type=List.CUSTOM).order_by('-id')[:6]

    set_layout_session(request, "lists", "lists_index")

    return render(request, 'lists_list.html', {
        'popular_lists': popular_lists,
        'latest_lists': latest_lists
    })


def detail(request, list_id):
    current_list = List.objects.get(id=list_id)
    other_lists = List.objects.filter(user=current_list.user).exclude(id=list_id)
    list_movies = current_list.movies.all().order_by('-id')

    paginator = Paginator(list_movies, 24)

    page = request.GET.get('page')

    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        movies = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        movies = paginator.page(paginator.num_pages)

    set_layout_session(request, "movies", "lists_detail")

    return render(request, 'lists_detail.html', {
        'list': current_list,
        'list_movies': movies,
        'other_lists': other_lists
    })


@login_required
def add(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
            
        if form.is_valid():
            new_list = form.save(commit=False)
            new_list.user = request.user

            new_list.save()

            return redirect('/lists/%s' % new_list.id)
        else:
            print form.errors
    else:
        movies = Movie.objects.all()

        return render(request, 'lists_add.html', {
            'movies': movies
        })


@login_required
def delete(request, list_id):
    current_list = List.objects.get(id=list_id)

    if current_list.user == request.user and current_list.type == List.CUSTOM:
        current_list.delete()
    else:
        return redirect('/lists/%s' % current_list.id)

    return redirect('/lists')


@login_required
def add_movie(request):
    if request.method == 'POST':
        tmdb = TMDB(settings.TMDB_API_KEY)

        list_id = request.POST['list_id']
        tmdb_id = request.POST['tmdb_id']
       
        movie = tmdb.Movies(tmdb_id)
        response = movie.info()

        new_movie, created = Movie.objects.get_or_create(
            name=movie.title,
            thumbnail=movie.poster_path,
            synopsis=movie.overview,
            release_date=movie.release_date,
            tmdb=tmdb_id,
            imdb=movie.imdb_id
        )

        current_list = List.objects.get(id=list_id)

        if not current_list.movies.all().filter(tmdb=tmdb_id).exists():
            current_list.movies.add(new_movie)

        return redirect('/lists/%s' % list_id)
    else:
        return redirect('/lists')


@login_required
def change_privacy(request, list_privacy, list_id):
    current_list = List.objects.get(id=list_id)
    privacy = True if list_privacy == 'private' else False

    if current_list.user == request.user and current_list.type == List.CUSTOM:
        current_list.privacy = privacy

        current_list.save()

    return redirect('/lists/%s' % current_list.id)


@login_required
def import_list(request, list_id):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']

        reader = parse_csv_file(csv_file)

        titles = [row['Title'] for row in reader]

        import_imdb_list.delay(titles, list_id)

        return redirect('/lists/%s' % list_id)
    else:
        return render(request, 'lists_import.html', {
            'list_id': list_id
        })