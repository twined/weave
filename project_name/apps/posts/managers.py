# -*- coding: utf-8 -*-

from datetime import datetime
from django.db import models


class LatestPostsManager(models.Manager):

    def news_posts(self, count=3):
        return self.model.objects.all().filter(
            status=self.model.PS_PUBLISHED,
            post_type=self.model.PT_NEWS).order_by('-publish_at')[:count]

    def blog_posts(self, count=3):
        return self.model.objects.all().filter(
            status=self.model.PS_PUBLISHED,
            post_type=self.model.PT_BLOG)[:count]


class PublishedPostsManager(models.Manager):

    def get_query_set(self):
        qs = super(PublishedPostsManager, self).get_query_set()
        return qs.filter(status__exact=self.model.PS_PUBLISHED,
                publish_at__lte=datetime.now())
