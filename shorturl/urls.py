####################
# @author         Pierre-Henry Soria <ph7software@gmail.com>
# @copyright      Pierre-Henry Soria, All Rights Reserved.
# @license        GNU General Public License;
####################

from django.conf.urls import patterns, url

urlpatterns = patterns('shorturl.views',
    url(r'^$', 'list'), # one empty string indicates the root
    url(r'^new/?$', 'new'),
    url(r'^(?P<code>\w{4})/?$', 'redirect_to_url'), #(?P<code>\w{4}) capture 4 alphanumeric characters.
)
