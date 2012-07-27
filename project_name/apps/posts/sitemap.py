from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse_lazy
from .models import Post


class BlogIndexSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return [reverse_lazy('blog')]

    def location(self, obj):
        return obj

    def lastmod(self, obj):
        post = Post.objects.all().filter(
            post_type=Post.PT_BLOG,
            status=Post.PS_PUBLISHED).order_by('-updated')[:1]
        if post:
            return post[0].updated


class BlogPostSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Post.objects.filter(
            post_type=Post.PT_BLOG, status=Post.PS_PUBLISHED)

    def lastmod(self, obj):
        return obj.updated


class NewsIndexSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return [reverse_lazy('news')]

    def location(self, obj):
        return obj

    def lastmod(self, obj):
        post = Post.objects.all().filter(
            post_type=Post.PT_NEWS,
            status=Post.PS_PUBLISHED).order_by('-updated')[:1]
        if post:
            return post[0].updated


class NewsPostSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Post.objects.filter(
            post_type=Post.PT_NEWS, status=Post.PS_PUBLISHED)

    def lastmod(self, obj):
        return obj.updated
