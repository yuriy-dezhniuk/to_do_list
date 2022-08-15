from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'my_to_do_list/index.html', {
        'title': 'TO DO LIST 777',
    })

def task(request):
    return render(request, 'my_to_do_list/task.html', {
        'title': 'Title Task X',
        'description': """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""",
        'priority': 'P1',
    })
