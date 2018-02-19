# -*- coding: utf-8 -*-
from django import forms
from django.forms.widgets import RadioSelect
from layouter.models import ContainerPlugin


class ButtonSelectWidget(RadioSelect):
    FONT_MAPPER = {
        ContainerPlugin.FULL_WIDTH: u'full-width',
        ContainerPlugin.THREE_QUARTER_WIDTH: u'three-quarter',
        ContainerPlugin.TWO_THIRD_WIDTH: u'two-third',
        ContainerPlugin.HALF_WIDTH: u'half',
        ContainerPlugin.THIRD_WIDTH: u'third',
        ContainerPlugin.QUARTER_WIDTH: u'quarter',
    }
    option_template_name = 'layouter/radio_option.html'

    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        o = super(ButtonSelectWidget, self).create_option(name, value, label, selected, index, subindex, attrs)
        o['columns'] = [self.FONT_MAPPER[f] for f in ContainerPlugin.TYPE_COLUMNS[int(value)]]
        return o


class ContainerPluginForm(forms.ModelForm):
    class Meta:
        model = ContainerPlugin
        fields = ['container_type']
        widgets = {
            'container_type': ButtonSelectWidget
        }

    def clean(self):
        cleaned_data = super(ContainerPluginForm, self).clean()
        if cleaned_data['css_classes']:
            cleaned_data['css_classes'] = cleaned_data['css_classes'].strip()
        return cleaned_data
