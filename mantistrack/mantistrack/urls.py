# Core Django imports
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.decorators import login_required

# Third party imports
from photologue.models import Photo, Gallery
from utils.views import CustomRegistrationView

admin.autodiscover()

urlpatterns = patterns('',
                       # Project's app URLconf includes
                       url(r'^$', TemplateView.as_view(template_name='base.html')),
                       url(r'^mantises/', include('mantises.urls', namespace='mantises')),
                       url(r'^containers/', include('containers.urls', namespace='containers')),
                       url(r'^feeders/', include('feeders.urls', namespace='feeders')),
                       url(r'^notes/', include('notes.urls', namespace='notes')),

                       # Admin includes
                       url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
                       url(r'^asdfQWERzxcv/', include(admin.site.urls)),

                       # OAuth includes
                       url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),

                       # Django-registration
                       url(r'^users/password/reset/done/$',
                           'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
                       url(r'^users/password/change/done/$',
                           'django.contrib.auth.views.password_change_done', name='password_change_done'),
                       url(r'^users/password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
                           'django.contrib.auth.views.password_reset_confirm',
                           name='auth_password_reset_confirm'),
                       url(r'^password/reset/complete/$',
                           'django.contrib.auth.views.password_reset_complete',
                           name='password_reset_complete'),
                       url(r'^users/', include('registration.auth_urls', namespace='users')),
                       url(r'^registration/complete/$',
                           TemplateView.as_view(template_name='registration/registration_complete.html'),
                           name='registration_complete'),
                       url(r'^registration/activate/complete/$',
                           TemplateView.as_view(template_name='registration/activation_complete.html'),
                           name='registration_activation_complete'),
                       url(r'^registration/register/$', CustomRegistrationView.as_view(),
                           name='registration_register'),
                       url(r'^registration/',
                           include('registration.backends.default.urls', namespace='registration')),

                       # Photologue URLs
                       url(r'^photologue/photo/add/$', login_required(CreateView.as_view(model=Photo)),
                           name='add-photo'),
                       url(r'^photologue/gallery/add/$', login_required(CreateView.as_view(model=Gallery)),
                           name='add-gallery'),
                       url(r'^photologue/gallery/(?P<title_slug>.*)/edit',
                           login_required(UpdateView.as_view(model=Gallery, slug_field='title_slug',
                                                             slug_url_kwarg='title_slug')),
                           name='edit-gallery'),
                       url(r'^photologue/', include('photologue.urls')),

                       # Media URL
                       url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.MEDIA_ROOT}),
                       )
