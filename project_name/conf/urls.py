from django.conf.urls import patterns, include, url

from papermill.feeds import LatestUpdatesFeed

sitemaps = {
}

urlpatterns = patterns(
    '',
    url(
        '^posts/',
        include('papermill.urls', namespace="posts")),
    url(
        '^admin/',
        include('cerebrum.admin.admin_urls', namespace="admin")),

    url(
        r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps}),
    url(
        r'^rss/$',
        LatestUpdatesFeed()),
)
