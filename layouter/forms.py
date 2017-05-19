# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.forms.widgets import RadioSelect, ChoiceInput, RadioFieldRenderer
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

from layouter.models import ContainerPlugin


class ButtonChoiceInput(ChoiceInput):
    input_type = 'radio'

    # This maps the column width to the corresponding css classes.
    FONT_MAPPER = {
        ContainerPlugin.FULL_WIDTH: u'full-width',
        ContainerPlugin.THREE_QUARTER_WIDTH: u'three-quarter',
        ContainerPlugin.TWO_THIRD_WIDTH: u'two-third',
        ContainerPlugin.HALF_WIDTH: u'half',
        ContainerPlugin.THIRD_WIDTH: u'third',
        ContainerPlugin.QUARTER_WIDTH: u'quarter',
    }

    def __init__(self, *args, **kwargs):
        super(ButtonChoiceInput, self).__init__(*args, **kwargs)
        self.value = force_text(self.value)

    def render(self, name=None, value=None, attrs=None):
        if self.choice_value:
            spans = ['<span class="icon-admin {}"></span>'.format(self.FONT_MAPPER[f])
                     for f in ContainerPlugin.TYPE_COLUMNS[int(self.choice_value)]]
            self.choice_label = ' '.join(spans)
            self.choice_label += '</br>' + str(ContainerPlugin.CONTAINER_TYPES[int(self.choice_value)][1])
            self.choice_label = mark_safe(self.choice_label)
        return super(ButtonChoiceInput, self).render(name, value, attrs)


class ButtonSelectRenderer(RadioFieldRenderer):
    choice_input_class = ButtonChoiceInput


class ButtonSelectWidget(RadioSelect):
    renderer = ButtonSelectRenderer


class ContainerPluginForm(forms.ModelForm):
    class Meta:
        model = ContainerPlugin
        fields = ['container_type']
        widgets = {
            'container_type': ButtonSelectWidget
        }

    def clean(self):
        cleaned_data = super(ContainerPluginForm, self).clean()
        cleaned_data['css_classes'] = cleaned_data['css_classes'].strip()
        return cleaned_data
