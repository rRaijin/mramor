from __future__ import absolute_import, unicode_literals

from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel

from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class HomePage(Page):
    h1_text = models.CharField(max_length=255, blank=True, default='Main head')
    h2_text = models.CharField(max_length=255, blank=True, default='Second head')
    logotype = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    header_bg = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('h1_text', classname="full"),
        FieldPanel('h2_text', classname="full"),
        ImageChooserPanel('logotype'),
        ImageChooserPanel('header_bg'),
    ]
