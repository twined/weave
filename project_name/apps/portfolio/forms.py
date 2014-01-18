# -*- coding: utf-8 -*-

from portfolio.models import ImageSeries, ImageCategory
from imgin.forms import BaseImageCategoryForm, BaseImageSeriesForm


class ImageCategoryForm(BaseImageCategoryForm):
    class Meta:
        model = ImageCategory
        exclude = ('user',)


class ImageSeriesForm(BaseImageSeriesForm):
    class Meta:
        model = ImageSeries
        exclude = ('user', 'credits', 'order',)
