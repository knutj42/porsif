from mezzanine import template


register = template.Library()


@register.as_tag
def recent_news(limit=4):
    """
    Put a list of recently published News into the template context.
    Usage: {% recent_news 3 as recent_news %}
    """
    news = News.objects.published()
    return list(news[:limit])
