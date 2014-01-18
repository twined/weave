from django.core.urlresolvers import reverse_lazy
APP_ADMIN_URLS = {
    'url_base': 'portfolio',
    'namespace': 'portfolio',
}
APP_ADMIN_MENU = {
    'Portfolio': {
        'Oversikt': {
            'url': reverse_lazy('admin:portfolio:series-list'),
            'icon': 'icon-th-list',
            'order': 0,
        },
        'Legg til': {
            'url': reverse_lazy('admin:portfolio:series-create'),
            'icon': 'icon-picture',
            'order': 1,
        },
        'Kategorier': {
            'url': reverse_lazy('admin:portfolio:category-list'),
            'icon': 'icon-list',
            'order': 2,
        },
    }
}
