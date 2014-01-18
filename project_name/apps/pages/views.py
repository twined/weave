# -*- coding: utf-8 -*-

from django.views.generic import TemplateView

from hiver.views import CacheMixin


class TextTemplateView(TemplateView):
    def render_to_response(self, context, **response_kwargs):
        response_kwargs['content_type'] = 'text/plain'
        return super(TemplateView, self).render_to_response(
            context, **response_kwargs)


class AboutView(CacheMixin, TemplateView):
    """
    Returns the view for the about page
    """
    cache_path = 'pages.about'
    template_name = 'pages/about.html'
