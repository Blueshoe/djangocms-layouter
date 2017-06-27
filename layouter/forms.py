# -*- coding: utf-8 -*-
from django import forms
from django.forms.utils import flatatt
from django.forms.widgets import RadioSelect, ChoiceInput, RadioFieldRenderer, CheckboxInput
from layouter.models import ContainerPlugin
from django.utils.encoding import force_text
from django.utils.html import format_html
from django.utils.safestring import mark_safe


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


class DeviceIconCheckBoxWidget(CheckboxInput):
    ICON_MAPPING = {
        'disable_on_mobile': '<i class="fa fa-mobile" aria-hidden="true"></i>',
        'disable_on_tablet': '<i class="fa fa-tablet" aria-hidden="true"></i>',
        'disable_on_desktop': '<i class="fa fa-desktop" aria-hidden="true"></i>',
    }

    def render(self, name, value, attrs=None):
        rendered_input = super(DeviceIconCheckBoxWidget, self).render(name, value, attrs)
        rendered_icon = mark_safe(self.ICON_MAPPING.get(name))
        return '{}{} '.format(rendered_input, rendered_icon)


class ContainerPluginForm(forms.ModelForm):
    class Meta:
        model = ContainerPlugin
        fields = ['container_type']
        widgets = {
            'container_type': ButtonSelectWidget,
            'disable_on_mobile': DeviceIconCheckBoxWidget,
            'disable_on_tablet': DeviceIconCheckBoxWidget,
            'disable_on_desktop': DeviceIconCheckBoxWidget,
        }

    def clean(self):
        cleaned_data = super(ContainerPluginForm, self).clean()
        if cleaned_data['css_classes']:
            cleaned_data['css_classes'] = cleaned_data['css_classes'].strip()
        return cleaned_data
