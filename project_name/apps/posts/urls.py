from django.conf.urls.defaults import patterns, url
from .views import PostDetailView


urlpatterns = patterns('',
    url(r'^news/$', 'posts.views.list_news', name='news'),
    url(r'^news/(?P<slug>.*)$', PostDetailView.as_view(),
        {'post_type': 0}, name='news-detail'),
    url(r'^blog/$', 'posts.views.list_blogposts', name='blog'),
    url(r'^blog/(?P<slug>.*)$', PostDetailView.as_view(),
        {'post_type': 1}, name='blog-detail'),
)
