from django.contrib.sitemaps import Sitemap
from .models import ImageCategory, ImageSeries, PortfolioImage


class PortfolioCategoriesSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return ImageCategory.objects.all()

    def location(self, obj):
        return obj.get_absolute_url()

    def lastmod(self, obj):
        img = PortfolioImage.objects.all().filter(
            series__category=obj,
        ).order_by('-created')[:1]
        if img:
            return img[0].created


class PortfolioSeriesSitemap(Sitemap):
    changefreq = "never"
    priority = 0.6

    def items(self):
        return ImageSeries.objects.all()

    def location(self, obj):
        return obj.get_absolute_url()

    def lastmod(self, obj):
        img = PortfolioImage.objects.all().filter(
            series=obj,
        ).order_by('-created')[:1]
        if img:
            return img[0].created
