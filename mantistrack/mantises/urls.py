__author__ = 'archen'

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, DetailView

from mantises import views
from mantises.models import Molt

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

    url(r'^mymantises/$', views.mymantises, name='mymantises'),

    url(r'^(?P<mantis_id>\d+)/$', views.detail, name='detail-mantis'),
    url(r'^(?P<pk>\d+)/edit$', login_required(views.MantisUpdate.as_view()), name='edit-mantis'),
    url(r'^mymantises/add/$', login_required(views.MantisCreate.as_view()), name='add-mantis'),

    # Molt URLs
    url(r'^(?P<mantis_id>\d+)/molt/$', views.do_molt, name='molt'),
    url(r'^(?P<mantis_id>\d+)/molts/add/$', login_required(views.MoltCreate.as_view()), name='add-molt'),
    url(r'^molts/(?P<pk>\d+)/edit/$', login_required(views.MoltUpdate.as_view()), name='edit-molt'),
    url(r'^(?P<mantis_id>\d+)/molts/$', views.molt_history, name='molt-history'),

    # Breed URLs
    url(r'^breeds/$', views.breeds, name='breeds'),
    url(r'^breeds/(?P<breed_id>\d+)/$', views.breed_detail, name='detail-breed'),
    url(r'^breeds/add/$', login_required(views.BreedCreate.as_view()), name='add-breed'),
    url(r'^breeds/(?P<pk>\d+)/edit$', login_required(views.BreedUpdate.as_view()), name='edit-breed'),
)