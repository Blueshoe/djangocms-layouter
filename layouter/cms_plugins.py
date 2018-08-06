# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from cms.plugin_pool import plugin_pool
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase

from layouter.forms import ContainerPluginForm
from layouter.models import ContainerPlugin


logger = logging.getLogger(__name__)


class ContainerCMSPlugin(CMSPluginBase):
    render_template = 'layouter/container.html'
    name = _('Layouting Row')
    model = ContainerPlugin
    allow_children = True
    form = ContainerPluginForm
    change_form_template = 'layouter/change_form.html'

    fieldsets = (
        (None, {
            'fields': ('container_type', 'margin', 'equal_height')
        }),
        (_('Advanced'), {
            'classes': ('collapse',),
            'fields': ('css_classes',)
        })
    )

    def render(self, context, instance, placeholder):
        context['width'] = 12 - 2 * instance.margin
        return super(ContainerCMSPlugin, self).render(context, instance, placeholder)

    def get_render_template(self, context, instance, placeholder):
        try:
            version = settings.LAYOUTER_BOOTSTRAP_VERSION
        except AttributeError:
            logger.warn('You should define the following setting in order to prevent unexpected behavior with '
                        'djangocms-layouter: "LAYOUTER_BOOTSTRAP_VERSION" [3,4]')
            # Returning the bootstrap3 template in case the version is not explicitly set, to avoid migration issues.
            return 'layouter/bootstrap3/container.html'

        if int(version) == 3:
            return 'layouter/bootstrap3/container.html'
        return 'layouter/bootstrap4/container.html'


plugin_pool.register_plugin(ContainerCMSPlugin)
