from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'base.html')


def resume(request):
    my_dictionary = {
        'insert_me': 'Hello there, i am from views.py',
        'second': "this is the second message!"
    }
    return render(request, 'curriculum/resume.html', context=my_dictionary)
