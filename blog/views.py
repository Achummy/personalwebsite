from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blog/index.html', {})

def about(request):
    return render(request, 'blog/about.html', {})

def blog(request):
    return render(request, 'blog/blog.html', {})

def design_post(request):
    return render(request, 'blog/design_post.html', {})

def lifestyle_post(request):
    return render(request, 'blog/lifestyle_post.html', {})