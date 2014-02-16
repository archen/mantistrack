__author__ = 'archen'

# Core Django imports
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

# Third party imports

# App-specific imports
from containers import views

urlpatterns = patterns('',
    # Container URLs
    url(r'^$', views.index, name='index'),
    url(r'^containers/$', views.containers, name='containers'),
    url(r'^my-containers/$', views.my_containers, name='my-containers'),
    url(r'^(?P<container_id>\d+)/$', views.detail_container, name='detail-container'),
    url(r'^(?P<pk>\d+)/edit$', login_required(views.ContainerUpdate.as_view()), name='edit-container'),
    url(r'^my-containers/add/$', login_required(views.ContainerCreate.as_view()), name='add-container'),

    # ContainerType URLs
    url(r'^container-types/$', views.container_types, name='container-types'),
    url(r'^container-types/my-container-types/$', views.my_container_types, name='my-container-types'),
    url(r'^container-types/my-container-types/add/$', login_required(views.ContainerTypeCreate.as_view()),
        name='add-container-type'),
    url(r'^container-types/(?P<container_type_id>\d+)/$', views.detail_container_type, name='detail-container-type'),
    url(r'^container-types/(?P<pk>\d+)/edit$', login_required(views.ContainerTypeUpdate.as_view()),
        name='edit-container-type'),

    # EnvironmentReading URLs
    url(r'^(?P<container_id>\d+)/readings/(?P<pk>\d+)/$', views.detail_reading, name='detail-reading'),
    url(r'^(?P<container_id>\d+)/readings/add/$', login_required(views.EnvironmentReadingCreate.as_view()),
        name='add-reading'),
    url(r'^(?P<container_id>\d+)/readings/(?P<pk>\d+)/edit/$', login_required(views.EnvironmentReadingUpdate.as_view()),
        name='edit-reading'),
    url(r'^(?P<container_id>\d+)/readings/$', views.reading_history, name='reading-history'),
)