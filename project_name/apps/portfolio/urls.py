from django.conf.urls import patterns, url
from .views import (
    PortfolioSeriesView, PortfolioIndexView,
    PortfolioCategoryImageView
)

urlpatterns = patterns(
    'images.views',
    url(r'^$', PortfolioIndexView.as_view(), name="index"),
    url(r'^(?P<series_slug>[\w-]+)/(?P<pk>\d+)/$',
        PortfolioCategoryImageView.as_view(), name="view"),
    url(r'^(?P<series_slug>[\w-]+)/$',
        PortfolioSeriesView.as_view(), name="series-view"),
)
