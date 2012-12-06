####################
# @author         Pierre-Henry Soria <ph7software@gmail.com>
# @copyright      Pierre-Henry Soria, All Rights Reserved.
# @license        GNU General Public License;
####################

from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'main.views.home'),
    url(r'^contact/?$', 'main.views.contact'),
    url(r'^shorturl/', include('shorturl.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


# if we're in DEBUG mode, allow django to serve media
# This is considered inefficient and isn't secure.
from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
