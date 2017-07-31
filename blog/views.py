from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'blog/index.html', {})

def about(request):
    return render(request, 'blog/about.html', {})

def portfolio(request):
    return render(request, 'blog/portfolio.html', {})

def blog(request):
	return render(request, 'blog/blog.html', {})

def design_post(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).filter(category="Design").order_by('published_date')
	return render(request, 'blog/design_post.html', {'posts':posts})

def lifestyle_post(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).filter(category="Lifestyle").order_by('published_date')
	return render(request, 'blog/lifestyle_post.html', {'posts':posts})

def contact(request):
    return render(request, 'blog/contact.html', {})

def post(request, post_title):
	context_dict = {}
	try:
		posts = Post.objects.get(slug=post_title)
		context_dict['post_title'] = posts.title
		context_dict['posts'] = posts
	except Post.DoesNotExist:
		pass
	return render(request, 'blog/post.html', context_dict)