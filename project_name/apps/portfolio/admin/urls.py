from django.conf.urls import patterns, url

from portfolio.admin.views import (
    ImageCategoryListView, ImageCategoryCreateView,
    ImageCategoryUpdateView, ImageCategoryDeleteView,
    ImageCategorySortSeriesView, AJAXImageCategorySortSeriesUpdate,
)

from portfolio.admin.views import (
    ImageSeriesListView, ImageSeriesCreateView,
    ImageSeriesAddImagesView, ImageSeriesUploadView,
    ImageSeriesUpdateView, ImageSeriesSortImagesView,
    AJAXImageSeriesDeleteView,
)

from portfolio.admin.views import (
    ImageDeleteView, ImageDeleteMultipleView,
    ImageEditAttrsView, PortfolioImageToggleHiddenView
)


urlpatterns = patterns(
    'portfolio.admin.views',
    # categories -------------------------------------------------------
    url(r'^kategorier/oversikt/$',
        ImageCategoryListView.as_view(),
        name="category-list"),
    url(r'^kategorier/ny/$',
        ImageCategoryCreateView.as_view(),
        name="category-create"),
    url(r'^kategorier/endre/(?P<pk>\d+)$',
        ImageCategoryUpdateView.as_view(),
        name="category-update"),
    url(r'^kategorier/slett/(?P<pk>\d+)$',
        ImageCategoryDeleteView.as_view(),
        name="category-delete"),
    url(r'^kategorier/(?P<category_id>\d+)/sorter/$',
        ImageCategorySortSeriesView.as_view(),
        name="category-sortseries"),
    url(r'^kategorier/(?P<category_id>\d+)/sorter/oppdater/$',
        AJAXImageCategorySortSeriesUpdate.as_view(),
        name="category-sortseries-update"),

    # series -----------------------------------------------------------
    url(r'^serier/oversikt/$',
        ImageSeriesListView.as_view(),
        name="series-list"),
    url(r'^serier/oversikt/slett/$',
        AJAXImageSeriesDeleteView.as_view(),
        name="series-delete"),
    url(r'^serier/ny/$',
        ImageSeriesCreateView.as_view(),
        name="series-create"),
    url(r'^serier/legg-til-bilder/(?P<image_series_id>\d+)$',
        ImageSeriesAddImagesView.as_view(),
        name="series-addimages"),
    url(r'^serier/legg-til-bilder/(?P<image_series_id>\d+)/last-opp/$',
        ImageSeriesUploadView.as_view(),
        name="series-upload"),
    url(r'^serier/endre/(?P<image_series_id>\d+)/$',
        ImageSeriesUpdateView.as_view(),
        name="series-update"),
    url(r'^serier/endre/(?P<image_series_id>\d+)/slett/$',
        ImageDeleteView.as_view(),
        name="image-delete"),
    url(r'^serier/endre/(?P<image_series_id>\d+)/slett-mange/$',
        ImageDeleteMultipleView.as_view(),
        name="image-deletemultiple"),
    url(r'^serier/endre/(?P<image_series_id>\d+)/sorter/$',
        ImageSeriesSortImagesView.as_view(),
        name="image-sort"),
    url(r'^serier/endre/(?P<image_series_id>\d+)/attrs/$',
        ImageEditAttrsView.as_view(),
        name="image-editattrs"),
    url(r'^serier/endre/(?P<image_series_id>\d+)/toggle-hidden/$',
        PortfolioImageToggleHiddenView.as_view(),
        name="image-togglehidden"),
)
