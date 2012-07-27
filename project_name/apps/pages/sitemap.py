from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse_lazy


class PagesSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return [
            reverse_lazy('about'),
        ]

    def location(self, obj):
        return obj


class RootSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1.0

    def items(self):
        return ['/']

    def location(self, obj):
        return obj
