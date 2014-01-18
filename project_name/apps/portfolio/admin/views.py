# images.py

import json

from django.core.urlresolvers import reverse_lazy
from django.views.generic import View
from django.http import HttpResponse

from ..models import (PortfolioImage, ImageSeries,
                      ImageCategory)

from ..forms import ImageSeriesForm, ImageCategoryForm
from application.views import LoginRequiredMixin


from imgin.views import (
    AJAXBaseImageHandleUploadView, AJAXBaseImageDeleteView,
    AJAXBaseImageDeleteMultipleView
)

# categories
from imgin.views import (
    BaseImageCategoryListView, BaseImageCategoryCreateView,
    BaseImageCategoryUpdateView, BaseImageCategoryDeleteView,
    BaseImageCategorySortSeriesView,
    AJAXBaseImageCategorySortSeriesUpdate
)

# imageseries
from imgin.views import (
    BaseImageSeriesListView, BaseImageSeriesCreateView,
    BaseImageSeriesAddImagesView, BaseImageSeriesUpdateView,
    AJAXBaseImageSeriesDeleteView,
    AJAXBaseImageSortView
)

# categories -----------------------------------------------------------


class ImageCategoryListView(LoginRequiredMixin,
                            BaseImageCategoryListView):
    model = ImageCategory


class ImageCategoryCreateView(LoginRequiredMixin,
                              BaseImageCategoryCreateView):
    model = ImageCategory
    form_class = ImageCategoryForm
    success_url = reverse_lazy('admin:portfolio:category-list')


class ImageCategoryUpdateView(LoginRequiredMixin,
                              BaseImageCategoryUpdateView):
    model = ImageCategory
    form_class = ImageCategoryForm
    success_url = reverse_lazy('admin:portfolio:category-list')


class ImageCategoryDeleteView(LoginRequiredMixin,
                              BaseImageCategoryDeleteView):
    model = ImageCategory
    success_url = reverse_lazy('admin:portfolio:category-list')


class ImageCategorySortSeriesView(LoginRequiredMixin,
                                  BaseImageCategorySortSeriesView):
    model = ImageCategory

# imageseries ----------------------------------------------------------


class ImageSeriesListView(LoginRequiredMixin,
                          BaseImageSeriesListView):
    model = ImageSeries
    categories_object = ImageCategory.objects.all()


class ImageSeriesCreateView(LoginRequiredMixin,
                            BaseImageSeriesCreateView):
    model = ImageSeries
    form_class = ImageSeriesForm

    def get_success_url(self):
        return self.object.get_addimages_url()


class ImageSeriesAddImagesView(LoginRequiredMixin,
                               BaseImageSeriesAddImagesView):
    model = ImageSeries


class ImageSeriesUpdateView(LoginRequiredMixin,
                            BaseImageSeriesUpdateView):
    model = ImageSeries
    form_class = ImageSeriesForm
    template_name = 'portfolio/admin/imageseries_update.html'
    pk_url_kwarg = 'image_series_id'
    success_url = reverse_lazy('admin:portfolio:series-list')


class ImageSeriesSortImagesView(LoginRequiredMixin,
                                AJAXBaseImageSortView):
    model_to_sort = PortfolioImage


class ImageSeriesUploadView(LoginRequiredMixin,
                            AJAXBaseImageHandleUploadView):
    model = PortfolioImage


class AJAXImageSeriesDeleteView(LoginRequiredMixin,
                                AJAXBaseImageSeriesDeleteView):
    model = ImageSeries

# ----------------
# image
# ----------------


class ImageDeleteView(LoginRequiredMixin,
                      AJAXBaseImageDeleteView):
    model = PortfolioImage


class ImageDeleteMultipleView(LoginRequiredMixin,
                              AJAXBaseImageDeleteMultipleView):
    model = PortfolioImage


class ImageEditAttrsView(LoginRequiredMixin,
                         View):
    model = PortfolioImage

    def post(self, request, *args, **kwargs):
        if not request.POST.get('id'):
            return HttpResponse(json.dumps({
                'status': 500,
                'error_msg': 'No ID supplied!'
            }), mimetype="application/json")

        photo_id = request.POST.get('id')
        f = self.model.objects.get(pk=photo_id)

        f.title = request.POST.get('title')
        f.credits = request.POST.get('credits')

        f.save()

        return HttpResponse(json.dumps({
            'status': 200,
            'id': photo_id,
            'title': request.POST.get('title'),
            'credits': request.POST.get('credits')
        }), mimetype="application/json")


class PortfolioImageToggleHiddenView(LoginRequiredMixin, View):

    model = PortfolioImage

    def post(self, request, *args, **kwargs):
        if not request.POST.get('ids'):
            return json.dumps({
                'status': 500,
                'error_msg': 'No IDs supplied!'
            })

        ids = request.POST['ids'].split(',')
        for image_id in ids:
            img = self.model.objects.get(pk=image_id)
            img.hidden_in_index = not img.hidden_in_index
            img.save()

        return HttpResponse(json.dumps({
            'status': 200,
            'ids': ids
        }), mimetype="application/json")


class AJAXImageCategorySortSeriesUpdate(
    LoginRequiredMixin, AJAXBaseImageCategorySortSeriesUpdate
):
    '''
    AJAX: Sorts imageseries within a category
    '''
    model = ImageSeries
