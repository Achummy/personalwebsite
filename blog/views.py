from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from .forms import ContactForm

# Create your views here.
def index(request):
    return render(request, 'blog/index.html', {})

def about(request):
    return render(request, 'blog/about.html', {})

def portfolio(request):
    return render(request, 'blog/portfolio.html', {})

def blog(request, title):
	if title == 'design' or title == 'lifestyle':
		posts = Post.objects.filter(published_date__lte=timezone.now()).filter(category=title).order_by('published_date')
		return render(request, 'blog/generic_post.html', {'posts':posts, 'category':title})
	else:
		return render(request, 'blog/blog.html', {})

def contact(request):
	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			try:
				send_mail(subject, message, email, [''])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect('success')
	return render(request, 'blog/contact.html', {'form': form})

def post(request, title):
	context_dict = {}
	try:
		post = Post.objects.all().get(slug=title)
		context_dict['post'] = post
	except Post.DoesNotExist:
		pass
	return render(request, 'blog/post.html', context_dict)

def project(request, title):
	title = title.replace('-','')
	title = title.lower()
	return render(request, "blog/{}.html".format(title), {})

def success(request):
	return render(request, 'blog/success.html', {})