from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<title>[-\w]+)/$', views.game, name='game'),
]