from django.core.exceptions import ObjectDoesNotExist
from mezzanine.pages.models import Page, RichTextPage
from mezzanine.pages.page_processors import processor_for


def get_or_create_contentholder_page(title):
    contentholder, created = RichTextPage.objects.get_or_create(title = title)
    if created:
        contentholder.in_menus = False
        contentholder.in_sitemap = False
        contentholder.save()
    return contentholder


def common_elements(request):
    """Adds the pages that contains the content of the left and right panels.
    """
    return dict(main_logo=get_or_create_contentholder_page("main_logo"),
                left_panel=get_or_create_contentholder_page("left_panel"),
                right_panel=get_or_create_contentholder_page("right_panel"),
                footer_right=get_or_create_contentholder_page("footer_right"),
                footer_center=get_or_create_contentholder_page("footer_center"),
                footer_left=get_or_create_contentholder_page("footer_left"),
                )