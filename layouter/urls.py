# -*- coding: utf-8 -*-

from django.conf.urls import url

from layouter.views import ToggleGridView

urlpatterns = [
    url(r'^toggle-grid/', ToggleGridView.as_view(), name='toggle-grid')
]
