from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^portfolio/$', views.portfolio, name='portfolio'),
    url(r'^portfolio/(?P<title>[-\w]+)/$', views.project, name='project'),
    url(r'^blog/(?P<title>[-\w]*)/$', views.blog, name='blog'),
    url(r'^blog/post/(?P<title>[-\w]+)/$', views.post, name='post'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^contact/success/$', views.success, name='success'),
]