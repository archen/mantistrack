__author__ = 'archen'

# Core Django imports
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

# Third party imports

# App-specific imports
from notes import views

urlpatterns = patterns('',
    # Note URLs
    url(r'^add/(?P<content_type>[a-z]+)/(?P<object_id>\d+)/?next=(?P<next>[a-z/\d]+)$',
        login_required(views.NoteCreate.as_view()), name='add-note'),
    url(r'^(?P<pk>\d+)/edit$', login_required(views.NoteUpdate.as_view()),
        name='edit-note'),
)