from django.contrib.syndication.views import Feed
from .models import Post


class LatestUpdatesFeed(Feed):
    title = "{{ project_name }} - Updates"
    link = "/"
    description = "Latest news and posts from {{ project_name }}"

    def items(self):
        return Post.objects.all().filter(status=2).order_by('-created')[:10]

    def item_title(self, item):
        return item.header

    def item_description(self, item):
        return item.lead
