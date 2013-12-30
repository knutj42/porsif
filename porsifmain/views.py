from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from mezzanine.pages.models import RichTextPage
import mezzanine.pages.views


def homepage(request):
    # We want to display the "Hovedsiden" page at the root url, but it doesn't work to set that page's url to "/", since
    # it doesn't seem to be possible to have subpages on a page with the url "/". Instead we just render the hovedsiden
    # page here and return that response. In addition, we hide the "Home" menuitem via css.
    hovedsiden, created = RichTextPage.objects.get_or_create(slug="hovedsiden")
    if created:
        hovedsiden.title = "Hovedsiden"
        hovedsiden.content = "Dette er hovedsiden"
        hovedsiden.save()

    slug = hovedsiden.slug

    response = mezzanine.pages.views.page(request, slug, extra_context=dict(page=hovedsiden))


    return response