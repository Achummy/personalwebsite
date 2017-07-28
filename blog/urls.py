from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^portfolio/', views.portfolio, name='portfolio'),
    url(r'^blog/', views.blog, name='blog'),
    url(r'^blog/design_post/', views.design_post, name='design_post'),
    url(r'^blog/lifestyle_post/', views.lifestyle_post, name='lifestyle_post'),
    url(r'^contact/', views.contact, name='contact'),
]