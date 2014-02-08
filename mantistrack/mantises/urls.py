__author__ = 'archen'

from django.conf.urls import patterns, url

from mantises import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<mantis_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<mantis_id>\d+)/molt/$', views.molt, name='molt'),
)