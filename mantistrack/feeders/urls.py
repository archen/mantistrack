__author__ = 'archen'

# Core Django imports
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

# Third party imports

# App-specific imports
from feeders import views

urlpatterns = patterns('',
    # Feeder URLs
    url(r'^$', views.index, name='index'),
    url(r'^feeders/$', views.feeders, name='feeders'),
    url(r'^my-feeders/$', views.my_feeders, name='my-feeders'),
    url(r'^(?P<feeder_id>\d+)/$', views.detail_feeder, name='detail-feeder'),
    url(r'^(?P<pk>\d+)/edit$', login_required(views.FeederUpdate.as_view()), name='edit-feeder'),
    url(r'^my-feeders/add/$', login_required(views.FeederCreate.as_view()), name='add-feeder'),

    # Feedings URLs
    url(r'^feedings/my-feedings/add/$', login_required(views.FeedingCreate.as_view()),
        name='add-feeding'),
    url(r'^feedings/(?P<pk>\d+)/edit$', login_required(views.FeedingUpdate.as_view()),
        name='edit-feeding'),

    # Hatch URLs
    url(r'^(?P<batch_id>\d+)/hatches/add/$', login_required(views.HatchCreate.as_view()),
        name='add-hatch'),
    url(r'^(?P<batch_id>\d+)/hatches/(?P<pk>\d+)/edit/$', login_required(views.HatchUpdate.as_view()),
        name='edit-hatch'),
    url(r'^(?P<batch_id>\d+)/hatches/$', views.hatch_history, name='hatch-history'),

    # Batch URLs
    url(r'^my-batches/$', views.my_batches, name='my-batches'),
    url(r'^(?P<feeder_id>\d+)/batches/(?P<batch_id>\d+)/$', views.detail_batch, name='detail-batch'),
    url(r'^batches/add/$', login_required(views.BatchCreate.as_view()),
        name='add-batch'),
    url(r'^(?P<feeder_id>\d+)/batches/(?P<pk>\d+)/edit/$', login_required(views.BatchUpdate.as_view()),
        name='edit-batch'),
)