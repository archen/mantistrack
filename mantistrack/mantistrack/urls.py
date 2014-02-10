from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.decorators import login_required


from photologue.models import Photo, Gallery

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', TemplateView.as_view(template_name='base.html')),
                       url(r'^mantises/', include('mantises.urls', namespace="mantises")),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),

                       url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
                       url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}),

                       url(r'^photologue/photo/add/$', login_required(CreateView.as_view(model=Photo)),
                           name='add-photo'),
                       url(r'^photologue/gallery/add/$', login_required(CreateView.as_view(model=Gallery)),
                           name='add-gallery'),
                       url(r'^photologue/gallery/(?P<title_slug>.*)/edit',
                           login_required(UpdateView.as_view(model=Gallery, slug_field='title_slug',
                                                             slug_url_kwarg='title_slug')),
                           name='edit-gallery'),
                       url(r'^photologue/', include('photologue.urls')),
                       url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.MEDIA_ROOT}),
                       )
