# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from cms.constants import RIGHT


@toolbar_pool.register
class LayouterModifier(CMSToolbar):

    def populate(self):
        # classes for scripting and styling
        extra_classes = ['js-layouterMenu', 'layouter-menuButton']
        # Button should have active state if grid is shown
        if self.request.session.get('layouter_grid'):
            extra_classes.append('cms-btn-active')
        self.toolbar.add_button('Toggle Grid', '', side=RIGHT, extra_classes=extra_classes)
