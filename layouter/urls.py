# -*- coding: utf-8 -*-
from django.urls import re_path

from layouter.views import ToggleGridView


app_name = 'layouter'


urlpatterns = [
    re_path(r'^toggle-grid/', ToggleGridView.as_view(), name='toggle-grid')
]
