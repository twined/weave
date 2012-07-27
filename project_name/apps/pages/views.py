# -*- coding: utf-8 -*-
'''
// {{ project_name }}
// view definitions for the pages app
// (c) Twined/Univers 2009-2012. All rights reserved.
'''

from django.views.generic import TemplateView

from hiver.views import CacheMixin


class AboutView(CacheMixin, TemplateView):
    template_name = 'pages/about.html'
    cache_path = '{{ project_name }}.pages.about'
