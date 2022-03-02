# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from layouter.views import ToggleGridView
from django.urls import path

urlpatterns = [
    path('toggle-grid/', ToggleGridView.as_view(), name='toggle-grid')
]
