__author__ = 'archen'

# Core Django imports
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

# Third party imports

# App-specific imports
from mantises import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

    # Mantis URLs
    url(r'^my-mantises/$', views.my_mantises, name='my-mantises'),
    url(r'^(?P<mantis_id>\d+)/$', views.detail_mantis, name='detail-mantis'),
    url(r'^(?P<pk>\d+)/edit$', login_required(views.MantisUpdate.as_view()), name='edit-mantis'),
    url(r'^my-mantises/add/$', login_required(views.MantisCreate.as_view()), name='add-mantis'),

    # Molt URLs
    url(r'^(?P<mantis_id>\d+)/molt/$', views.do_molt, name='molt'),
    url(r'^(?P<mantis_id>\d+)/molts/add/$', login_required(views.MoltCreate.as_view()), name='add-molt'),
    url(r'^molts/(?P<pk>\d+)/edit/$', login_required(views.MoltUpdate.as_view()), name='edit-molt'),
    url(r'^(?P<mantis_id>\d+)/molts/$', views.molt_history, name='molt-history'),

    # Breed URLs
    url(r'^breeds/$', views.breeds, name='breeds'),
    url(r'^breeds/(?P<breed_id>\d+)/$', views.detail_breed, name='detail-breed'),
    url(r'^breeds/add/$', login_required(views.BreedCreate.as_view()), name='add-breed'),
    url(r'^breeds/(?P<pk>\d+)/edit$', login_required(views.BreedUpdate.as_view()), name='edit-breed'),

    # Ooth URLs
    url(r'^ooths/$', views.my_ooths, name='my-ooths'),
    url(r'^(?P<mantis_id>\d+)/ooths/(?P<ooth_id>\d+)/$', views.detail_ooth, name='detail-ooth'),
    url(r'^(?P<mantis_id>\d+)/ooths/add/$', login_required(views.OothCreate.as_view()), name='add-ooth'),
    url(r'^ooths/(?P<pk>\d+)/edit$', login_required(views.OothUpdate.as_view()), name='edit-ooth'),
)