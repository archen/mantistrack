__author__ = 'archen'

from django.conf.urls import patterns, url, include
from photologue.models import Photo, Gallery, GalleryUpload
from django.views.generic import CreateView

from mantises import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<mantis_id>\d+)/$', views.detail, name='detail'),
)