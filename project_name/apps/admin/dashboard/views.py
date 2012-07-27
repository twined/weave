# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.contrib import messages

from {{ project_name }}.apps.application.views import LoginRequiredMixin


class DashboardIndex(LoginRequiredMixin, TemplateView):
    """
    Presents the admin dashboard.
    """
    template_name = 'dashboard/templates/dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardIndex, self).get_context_data(**kwargs)
        return context
