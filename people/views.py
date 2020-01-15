from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User

from lists.models import List

from utils import set_layout_session


def index(request):
    popular_people = User.objects.order_by('-id')
    latest_people = User.objects.order_by('-id')

    set_layout_session(request, "people", "people_index")

    return render(request, 'people_list.html', {
        'popular_people': popular_people,
        'latest_people': latest_people    
    })


def detail(request, user_id):
    person = User.objects.get(id=user_id)
    public_lists = List.objects.filter(user=user_id, type=List.CUSTOM, privacy=False)
    favorite_list = List.objects.get(user=user_id, type=List.FAVORITE)
    seen_list = List.objects.get(user=user_id, type=List.SEEN)
    must_see_list = List.objects.get(user=user_id, type=List.MUST_SEE)

    return render(request, 'people_detail.html', {
        'favorite_list': favorite_list,
        'seen_list': seen_list,
        'must_see_list': must_see_list,
        'person': person,
        'public_lists': public_lists
    })
