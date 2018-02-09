from django.db import models
from django.utils import timezone
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class Portfolio(Page):
    date = models.DateField("Posted date", default=timezone.now)
    project_name = models.CharField(max_length=255)
    link_name = models.CharField(max_length=100, blank=True, default='more')
    desc = models.TextField(blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('project_name'),
        FieldPanel('link_name'),
        FieldPanel('desc'),
        InlinePanel('portfolio_images', label="Portfolio images"),
    ]

    def main_image(self):
        gallery_item = self.portfolio_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None


class PortfolioGalleryImage(Orderable):
    page = ParentalKey(Portfolio, related_name='portfolio_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]