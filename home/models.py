from __future__ import absolute_import, unicode_literals

from django.apps import apps
from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel

from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet

from home.forms import ContactForm


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

    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        portfolio_list = apps.get_model('portfolio', 'Portfolio')
        context['portfolio'] = portfolio_list.objects.all().order_by('-date')[:4]
        context['feedback_form'] = ContactForm()
        return context


@register_snippet
class OurSkills(models.Model):
    title = models.TextField(max_length=30, blank=True)
    desc = models.TextField(max_length=200, blank=True)
    skill_logo = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('title'),
        FieldPanel('desc'),
        ImageChooserPanel('skill_logo'),
    ]

    def __str__(self):
        return self.title
