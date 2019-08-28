from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Brian Hanna',
        'title': 'Learn Django',
        'content': 'Simple Django blog app',
        'date_posted': 'June 12, 2019'
    },
{
        'author': 'Joe Rogan',
        'title': 'Joe Rogan Podcast',
        'content': 'Podcast... ALL DAY',
        'date_posted': 'July 4, 2019'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
