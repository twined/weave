# Create your views here.
# -*- coding: utf-8 -*-

from django.views.generic import TemplateView, DetailView

from hiver.views import CacheMixin
from .models import PortfolioImage, ImageSeries


class PortfolioCategoryList(CacheMixin, TemplateView):
    """
    Returns the view for Portfolio category or all
    """
    cache_path = 'portfolio.list'
    template_name = 'portfolio/portfoliocategory_list.html'

    def get_context_data(self, **kwargs):
        page_title = ''
        context = super(PortfolioCategoryList, self).get_context_data(**kwargs)
        if 'category_slug' in self.kwargs:
            images = PortfolioImage.objects.select_related().filter(
                series__category__slug=self.kwargs['category_slug']
            )
            page_title = self.kwargs['category_slug']

        start = 0
        end = 40
        if 'page' in self.request.GET:
            page = int(self.request.GET['page'])
            start = (start + (page - 1)) * 40
            end = (page) * 40
        context['images'] = images[start:end]
        context['page_title'] = page_title

        return context


class PortfolioCategoryImageView(CacheMixin, DetailView):
    """
    Returns a view for a single image. Also fetches the other images
    in the same set, if any.
    """
    model = PortfolioImage
    context_object_name = 'image'
    cache_path = 'portfolio.view'
    template_name = 'portfolio/portfolioimage_view.html'

    def get_context_data(self, **kwargs):
        context = super(PortfolioCategoryImageView,
                        self).get_context_data(**kwargs)
        context['image_series'] = self.object.series.related_images.all()

        for index, item in enumerate(context['image_series']):
            if item == context['image']:
                try:
                    context['next_image'] = \
                        context['image_series'].all()[index + 1]
                except IndexError:
                    context['next_image'] = context['image_series'].all()[0]

        return context


class PortfolioSeriesView(CacheMixin, TemplateView):
    """
    Returns a view for a series. Also fetches the other images
    in the same set, if any.
    """
    model = ImageSeries
    cache_path = 'imageseries.view'
    template_name = 'portfolio/portfolioimage_view.html'

    def get_context_data(self, **kwargs):
        context = super(PortfolioSeriesView, self).get_context_data(**kwargs)
        context['image_series'] = ImageSeries.objects.get(
            slug=self.kwargs['series_slug']
        ).related_images.all()
        if context['image_series']:
            context['image'] = context['image_series'][0]
            try:
                context['next_image'] = context['image_series'][1]
            except IndexError:
                context['next_image'] = context['image']
        return context


class PortfolioIndexView(CacheMixin, TemplateView):
    """
    Returns a view for a series. Also fetches the other images
    in the same set, if any.
    """
    model = ImageSeries
    cache_path = 'imageseries.index'
    template_name = 'portfolio/portfolio_index.html'

    def get_context_data(self, **kwargs):
        context = super(PortfolioIndexView, self).get_context_data(**kwargs)
        image_series = ImageSeries.objects.all().order_by('order')
        context['image_series'] = image_series
        return context
