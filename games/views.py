from django.shortcuts import render, redirect

# Create your views here.
def game(request, title):
    return render(request, 'games/{}.html'.format(title), {})

