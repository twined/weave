# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save, post_delete

import imgin.settings
from imgin.models import (
    BaseImage, BaseImageCategory, BaseImageSeries
)


class ImageCategory(BaseImageCategory):
    '''
    Editorials/Portraits/Commercial
    '''

    @staticmethod
    def get_create_url(*args, **kwargs):
        return reverse('admin:portfolio:category-create')

    @property
    def get_update_url(self):
        return reverse(
            'admin:portfolio:category-update',
            kwargs={'pk': self.pk}
        )

    @property
    def get_delete_url(self):
        return reverse(
            'admin:portfolio:category-delete',
            kwargs={'pk': self.pk}
        )

    @property
    def get_sortseries_url(self):
        return reverse(
            'admin:portfolio:category-sortseries',
            kwargs={'category_id': self.pk}
        )

    def get_absolute_url(self):
        return reverse(
            'portfolio:category-list',
            kwargs={'category_slug': self.slug}
        )

    class Meta:
        verbose_name = "Portfoliokategori"
        verbose_name_plural = "Portfoliokategorier"


class ImageSeries(BaseImageSeries):
    '''
    A set of photos that belong together. I.E. a shoot for Vogue.
    '''
    category = models.ForeignKey(ImageCategory, verbose_name=u'Kategori')

    @staticmethod
    def get_create_url():
        return reverse(
            'admin:portfolio:series-create'
        )

    def get_update_url(self):
        return reverse(
            'admin:portfolio:series-update',
            kwargs={'image_series_id': self.pk}
        )

    def get_addimages_url(self):
        return reverse(
            'admin:portfolio:series-addimages',
            kwargs={'image_series_id': self.pk}
        )

    def get_upload_url(self):
        return reverse(
            'admin:portfolio:series-upload',
            kwargs={'image_series_id': self.pk}
        )

    def get_absolute_url(self):
        return reverse(
            'portfolio:series-view',
            kwargs={
                'series_slug': self.slug,
            }
        )

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Bildeserie'
        verbose_name_plural = 'Bildeserier'
        ordering = ['category', 'order', '-created']


from .signals import invalidate_portfolio_cache

post_save.connect(
    invalidate_portfolio_cache, sender=ImageSeries,
    dispatch_uid="ImageSeries.post_save.invalidate"
)
post_delete.connect(
    invalidate_portfolio_cache, sender=ImageSeries,
    dispatch_uid="ImageSeries.post_delete.invalidate"
)


class PortfolioImage(BaseImage):
    series = models.ForeignKey(ImageSeries, related_name='related_images')
    IMGIN_KEY = 'portfolio'
    IMGIN_CFG = imgin.settings.IMGIN_CONFIG[IMGIN_KEY]
    title = models.CharField('Tittel', max_length=255,
                             null=True, blank=True)
    credits = models.CharField('Krediteringer', max_length=255,
                               null=True, blank=True)
    hidden_in_index = models.BooleanField(default=False)

    def get_dir_qualifier(self):
        '''
        this returns the specification of the models upload dir
        i.e. if it's part of a series, it could be /images/SERIES_ID/
        '''
        return self.series.id

    def populate(self, request, **kwargs):
        self.series_id = kwargs['image_series_id']
        self.user_id = request.user.pk
        self.order = 0

    def get_absolute_url(self):
        return reverse(
            'portfolio:view',
            kwargs={
                'series_slug': self.series.slug,
                'pk': self.pk
            }
        )

    @staticmethod
    def get_delete_url():
        return reverse(
            'admin:portfolio:image-delete'
        )

    class Meta:
        ordering = ['series__category', 'series__order', 'order', '-created']

# connect signals
post_save.connect(
    invalidate_portfolio_cache, sender=PortfolioImage,
    dispatch_uid="PortfolioImage.post_save.invalidate"
)
post_delete.connect(
    invalidate_portfolio_cache, sender=PortfolioImage,
    dispatch_uid="PortfolioImage.post_delete.invalidate"
)
