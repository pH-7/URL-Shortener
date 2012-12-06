####################
# @author         Pierre-Henry Soria <ph7software@gmail.com>
# @copyright      Pierre-Henry Soria, All Rights Reserved.
# @license        GNU General Public License;
####################

from django.shortcuts import redirect, get_object_or_404, render

def home(request):
    return render(request, 'main/home.html', locals())

def contact(request):
    return render(request, 'main/contact.html', locals())
