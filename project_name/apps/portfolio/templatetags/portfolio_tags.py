from django import template

from portfolio.models import PortfolioImage

register = template.Library()


@register.inclusion_tag('portfolio/templatetags/latest_images.html',
                        takes_context=True)
def latest_images(context):
    """
    Renders latest posts overview
    """

    images = PortfolioImage.objects.all()[:12]

    return {
        'images': images,
    }
