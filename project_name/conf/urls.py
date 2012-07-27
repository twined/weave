from django.conf.urls import patterns, include, url

from pages.sitemap import PagesSitemap, RootSitemap
from posts.sitemap import (BlogPostSitemap, NewsPostSitemap,
    BlogIndexSitemap, NewsIndexSitemap)
from posts.feeds import LatestUpdatesFeed

sitemaps = {
    'root': RootSitemap,
    'blog': BlogPostSitemap,
    'blog_index': BlogIndexSitemap,
    'news_index': NewsIndexSitemap,
    'news': NewsPostSitemap,
    'pages': PagesSitemap,
}

urlpatterns = patterns('',
    url(r'^app/', include('app.urls')),

    url('^posts/', include('posts.urls', namespace="posts")),
    url('^admin/', include('admin.urls', namespace="admin")),

    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
            {'sitemaps': sitemaps}),
    (r'^rss/$', LatestUpdatesFeed()),
)
