####################
# @author         Pierre-Henry Soria <ph7software@gmail.com>
# @copyright      Pierre-Henry Soria, All Rights Reserved.
# @license        GNU General Public License;
####################

from django.db import models
from django.utils.translation import ugettext_lazy as _

class ShortURL(models.Model):
    url = models.URLField(verbose_name= _("Your URL to shorten"), unique=True)
    code = models.CharField(max_length=4, unique=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name= _("Date of registration"))
    nb_access = models.IntegerField(default=0, verbose_name= _("Number of accesses to the URL"))

    def __unicode__(self):
        return "[{0}] {1}".format(self.code, self.url)

    class Meta:
        verbose_name = _("Short URL")
        verbose_name_plural = _("Short URLs")
