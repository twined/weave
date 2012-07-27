# -*- coding: utf-8 -*-

'''
// {{ project_name }}
// model definitions for the posts app
// (c) Twined/Univers 2009-2012. All rights reserved.
'''

from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, post_delete

from .managers import LatestPostsManager, PublishedPostsManager


class Post(models.Model):
    """
    Post model for blog and news apps
    """
    PS_DRAFT = 0
    PS_WAITING = 1
    PS_PUBLISHED = 2
    PS_DELETED = 3

    POST_STATUS_TYPES = (
        (PS_DRAFT, 'Kladd'),
        (PS_WAITING, 'Venter'),
        (PS_PUBLISHED, 'Publisert'),
        (PS_DELETED, 'Slettet'),
    )

    PT_NEWS = 0
    PT_BLOG = 1

    POST_TYPES = (
        (PT_NEWS, 'Nyhetsartikkel'),
        (PT_BLOG, 'Blogginnlegg'),
    )

    post_type = models.IntegerField(
            choices=POST_TYPES, default=0, verbose_name="Post type")
    header = models.CharField(
            max_length=255, null=False, blank=False,
            verbose_name='Overskrift')
    slug = models.CharField(max_length=255, verbose_name="URL")
    lead = models.TextField(verbose_name='Ingress')
    body = models.TextField(verbose_name="Brødtekst")
    user = models.ForeignKey(User, verbose_name="Bruker")
    status = models.IntegerField(
            choices=POST_STATUS_TYPES, default=0, verbose_name='Status')
    created = models.DateTimeField(
            auto_now_add=True, verbose_name="Opprettet")
    updated = models.DateTimeField(auto_now=True, verbose_name="Endret")
    publish_at = models.DateTimeField(
            default=datetime.now, verbose_name='Publiseringstidspunkt')
    published = models.DateTimeField(
            null=True, blank=True, editable=False,
            verbose_name='Publisert')
    tweeted = models.BooleanField(
            null=False, blank=False, default=False, editable=False)

    objects = models.Manager()
    latest = LatestPostsManager()
    published = PublishedPostsManager()

    @property
    def status_class(self):
        return self.POST_STATUS_TYPES[self.status][1]

    @models.permalink
    def get_absolute_url(self):
        return ('news-detail', [self.slug]) \
                if self.post_type == self.PT_NEWS else \
                ('blog-detail', [self.slug])

    class Meta:
        ordering = ('-created',)

# connect signals
from .signals import invalidate_cache
post_save.connect(invalidate_cache, sender=Post,
        dispatch_uid="Post.post_save.invalidate")
post_delete.connect(invalidate_cache, sender=Post,
        dispatch_uid="Post.post_delete.invalidate")


class PostCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.CharField(max_length=255)
    user = models.ForeignKey(User)
    created = models.DateTimeField(
            default=datetime.now, editable=False)
    modified = models.DateTimeField(
            default=datetime.now, editable=False)
