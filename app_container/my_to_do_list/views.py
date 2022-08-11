from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'my_to_do_list/index.html', {
        'title': 'TO DO LIST 777',
    })
