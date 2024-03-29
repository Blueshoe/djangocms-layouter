# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.safestring import mark_safe
from cms.models.pluginmodel import CMSPlugin
from easy_thumbnails.files import get_thumbnailer
from filer.fields.image import FilerImageField
from django.utils.translation import gettext_lazy as _
from django.utils.encoding import force_str
from six import python_2_unicode_compatible


@python_2_unicode_compatible
class ContainerPlugin(CMSPlugin):

    FULL_WIDTH = 100
    THREE_QUARTER_WIDTH = 75
    TWO_THIRD_WIDTH = 66
    HALF_WIDTH = 50
    THIRD_WIDTH = 33
    QUARTER_WIDTH = 25

    NO_MARGIN = _('No margin')
    ONE_COL_MARGIN = '8.33%'
    TWO_COL_MARGIN = '16.66%'
    THREE_COL_MARGIN = '25%'
    FOUR_COL_MARGIN = '33.33%'

    CONTAINER_TYPES = [
        (0, _('One tile - full width')),
        (1, _('Two tiles - 50 | 50')),
        (2, _('Two tiles - 25 | 75')),
        (3, _('Two tiles - 75 | 25')),
        (4, _('Two tiles - 33 | 66')),
        (5, _('Two tiles - 66 | 33')),
        (6, _('Three tiles - 33 | 33 | 33')),
        (7, _('Three tiles - 25 | 25 | 50')),
        (8, _('Three tiles - 25 | 50 | 25')),
        (9, _('Three tiles - 50 | 25 | 25')),
        (10, _('Four tiles - 25 | 25 | 25 | 25')),
    ]

    TYPE_COLUMNS = {
        0: [FULL_WIDTH],
        1: [HALF_WIDTH, HALF_WIDTH],
        2: [QUARTER_WIDTH, THREE_QUARTER_WIDTH],
        3: [THREE_QUARTER_WIDTH, QUARTER_WIDTH],
        4: [THIRD_WIDTH, TWO_THIRD_WIDTH],
        5: [TWO_THIRD_WIDTH, THIRD_WIDTH],
        6: [THIRD_WIDTH, THIRD_WIDTH, THIRD_WIDTH],
        7: [QUARTER_WIDTH, QUARTER_WIDTH, HALF_WIDTH],
        8: [QUARTER_WIDTH, HALF_WIDTH, QUARTER_WIDTH],
        9: [HALF_WIDTH, QUARTER_WIDTH, QUARTER_WIDTH],
        10: [QUARTER_WIDTH, QUARTER_WIDTH, QUARTER_WIDTH, QUARTER_WIDTH]
    }

    MARGIN_TYPES = (
        (0, NO_MARGIN),
        (1, ONE_COL_MARGIN),
        (2, TWO_COL_MARGIN),
        (3, THREE_COL_MARGIN),
        (4, FOUR_COL_MARGIN)
    )

    NO_PARALLAX = 0
    CSS_PARALLAX = 1
    TRUE_PARALLAX = 2
    BACKGROUND_IMAGE_PARALLAX_CHOICES = (
        (NO_PARALLAX, _('No effect')),
        (CSS_PARALLAX, _('Static background image')),
        (TRUE_PARALLAX, _('Parallax background image')),
    )

    container_type = models.IntegerField(choices=CONTAINER_TYPES, null=False, blank=False, default=TYPE_COLUMNS[0])

    margin = models.IntegerField(choices=MARGIN_TYPES, null=False, blank=False, default=MARGIN_TYPES[0][0],
                                 help_text=_('How much margin is needed on the left and right side?'))

    background_image = FilerImageField(
        verbose_name=_('Background image'),
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    background_image_parallax = models.IntegerField(_('Parallax Effect'), null=False, blank=False,
                                                    choices=BACKGROUND_IMAGE_PARALLAX_CHOICES, default=NO_PARALLAX)

    background_image_width = models.IntegerField(_('Background image width'), null=True, blank=True, default=1920)
    background_image_height = models.IntegerField(_('Background image width'), null=True, blank=True, default=1080,
                                                  help_text=_('It is recommended to limit the size of the background '
                                                              'image to a reasonable number in order to reduce page '
                                                              'loading times.'))

    # To achieve same height columns we use the CSS3 flex box grid. For more information about it have a look at
    # http://caniuse.com/flexbox
    equal_height = models.BooleanField(verbose_name=_('Align Content Height'),
                                       help_text=_('Align height of all columns in this row. Please note: '
                                                   'This setting is not  supported by Internet Explorer 9 and below.'),
                                       null=False, blank=False, default=False)

    css_classes = models.CharField(max_length=512, blank=True, null=True)

    @property
    def max_children(self):
        return len(self.TYPE_COLUMNS[self.container_type])

    def get_resized_background_image(self):
        """
        :return: The image which is thumbnailed to the specified size via easy-thumbnails
        """
        if self.background_image is None:
            return None

        thumbnail_options = {
            'crop': False,
            'size': (self.background_image_width, self.background_image_height)
        }
        try:
            thumbnailer = get_thumbnailer(self.background_image)
            image = thumbnailer.get_thumbnail(thumbnail_options)
        except:
            return None
        else:
            return image

    def clean(self):
        super(ContainerPlugin, self).clean()
        if self.background_image_parallax is not self.NO_PARALLAX and not self.background_image:
            raise ValidationError(
                _('You need to specify a background image in order to use a parallax effect.')
            )

    def __str__(self):
        name = self.CONTAINER_TYPES[self.container_type][1]
        if self.num_children() > self.max_children:
            name = '<span style="color:red">Warning, too many tiles!</span> {}'.format(name)

        return mark_safe(force_str(name))
