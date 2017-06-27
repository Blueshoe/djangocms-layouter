# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from cms.api import add_plugin
from cms.models import Placeholder

from layouter.cms_plugins import ContainerCMSPlugin
from layouter.models import ContainerPlugin


class LayouterPluginTests(TestCase):

    def setUp(self):
        self.placeholder = Placeholder.objects.create(slot='test')
        self.model_instance = add_plugin(
            self.placeholder,
            ContainerCMSPlugin,
            'en',
            container_type=ContainerPlugin.CONTAINER_TYPES[0][0],
            margin=ContainerPlugin.MARGIN_TYPES[1][0]
        )
        self.plugin_instance = self.model_instance.get_plugin_class_instance()

    def test_plugin_context(self):
        context = self.plugin_instance.render({}, self.model_instance, None)
        self.assertIn('width', context)
        self.assertEqual(context['width'], 10)

    def test_plugin_title(self):
        print('Check if __str__ implementation works fine: ' + str(self.model_instance))
