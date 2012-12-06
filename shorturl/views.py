####################
# @author         Pierre-Henry Soria <ph7software@gmail.com>
# @copyright      Pierre-Henry Soria, All Rights Reserved.
# @license        GNU General Public License;
####################

from django.shortcuts import redirect, get_object_or_404, render
from models import ShortURL
from forms import ShortURLForm
import random, string

def generate(nb):
    characters = string.letters + string.digits
    aleatory = [random.choice(characters) for _ in xrange(nb)]

    return ''.join(aleatory)

def list(request):
    """Showing redirects"""
    shorten = ShortURL.objects.order_by('-nb_access')

    return render(request, 'shorturl/list.html', locals())

def new(request):
    """Adding a redirection"""
    if request.method == "POST":
        form = ShortURLForm(request.POST)
        if form.is_valid():
            short = form.save(commit=False)
            short.code = generate(4) # Number of characters
            short.save()

            return redirect(list)
    else:
        form = ShortURLForm()

    return render(request, 'shorturl/new.html', {'form':form})

def redirect_to_url(request, code):
    """Redirect to the URL saved"""
    short = get_object_or_404(ShortURL, code=code)
    short.nb_access += 1
    short.save()

    return redirect(short.url, permanent=True)
