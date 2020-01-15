from django.shortcuts import render
from django.views.generic.base import TemplateView

from lists.models import List


def index(request):
    my_lists = List.objects.filter(user=request.user) if request.user.username else []

    return render(request, 'home.html', {
        'my_lists': my_lists
    })
