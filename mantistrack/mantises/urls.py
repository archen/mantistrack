__author__ = 'archen'

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, DetailView

from mantises import views
from mantises.models import Molt

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<mantis_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>\d+)/edit$', login_required(views.MantisUpdate.as_view()), name='edit'),
    url(r'^mymantises/$', views.mymantises, name='mymantises'),
    url(r'^mymantises/add/', login_required(views.MantisCreate.as_view()), name='add'),
    url(r'^(?P<mantis_id>\d+)/molt/$', views.molt, name='molt'),
#    url(r'^molt/(?P<pk>\d+)/$', login_required(DetailView.as_view(model=Molt)), name='molt-view'),
    url(r'^molt/(?P<pk>\d+)/edit/$', login_required(UpdateView.as_view(model=Molt)), name='edit-molt'),
    url(r'^(?P<mantis_id>\d+)/molt-history/$', views.molt_history, name='molt-history'),
)