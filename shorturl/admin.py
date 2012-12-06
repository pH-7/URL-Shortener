####################
# @author         Pierre-Henry Soria <ph7software@gmail.com>
# @copyright      Pierre-Henry Soria, All Rights Reserved.
# @license        GNU General Public License;
####################

from django.contrib import admin
from models import ShortURL

class ShortURLAdmin(admin.ModelAdmin):
    list_display   = ('url', 'code', 'date', 'nb_access')
    date_hierarchy = 'date'
    ordering       = ('date',)
    search_fields  = ('url',)

admin.site.register(ShortURL, ShortURLAdmin)
