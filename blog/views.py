from django.core.mail import send_mail, BadHeaderError
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

def blog(request):
	return render(request, 'blog/blog.html', {})

def design_post(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).filter(category="Design").order_by('published_date')
	return render(request, 'blog/design_post.html', {'posts':posts})

def lifestyle_post(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).filter(category="Lifestyle").order_by('published_date')
	return render(request, 'blog/lifestyle_post.html', {'posts':posts})

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

def post(request, post_title):
	context_dict = {}
	try:
		posts = Post.objects.get(slug=post_title)
		context_dict['post_title'] = posts.title
		context_dict['posts'] = posts
	except Post.DoesNotExist:
		pass
	return render(request, 'blog/post.html', context_dict)

def success(request):
	return render(request, 'blog/success.html', {})