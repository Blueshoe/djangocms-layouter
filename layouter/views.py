# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http.response import JsonResponse
from django.views.generic.base import View


class ToggleGridView(View):

    def post(self, request, *args, **kwargs):
        # If a post is placed here, toggle the layouter_grid in the session.
        # This causes the button in the toolbar to be active or inactive and the grid to be shown or hidden.
        request.session['layouter_grid'] = not bool(request.session.get('layouter_grid'))
        # Return the result as JSON.
        res = {'show_grid': request.session['layouter_grid']}
        return JsonResponse(res, status=200)
