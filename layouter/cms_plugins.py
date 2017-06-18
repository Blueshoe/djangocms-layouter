# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase

from layouter.forms import ContainerPluginForm
from layouter.models import ContainerPlugin


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


plugin_pool.register_plugin(ContainerCMSPlugin)
