from django.utils.translation import ugettext_lazy as _

from feincms.module.page.models import Page
from feincms.content.application.models import ApplicationContent
from feincms.content.richtext.models import RichTextContent
from feincms.content.medialibrary.models import MediaFileContent

from pathways.models import Pathway


Page.register_extensions(
    'feincms.module.extensions.datepublisher',
    'feincms.module.extensions.translations'
)

Page.register_templates({
    'title': _('Standard template'),
    'path': 'base.html',
    'regions': (
        ('main', _('Main content area')),
        ('sidebar', _('Sidebar'), 'inherited'),
    ),
})

Page.create_content_type(RichTextContent)
Page.create_content_type(MediaFileContent, TYPE_CHOICES=(
    ('default', _('default')),
    ('lightbox', _('lightbox')),
))
Page.create_content_type(ApplicationContent, APPLICATIONS=(
    ('elephantblog', _('Blog'), {'urls': 'elephantblog.urls'}),
    ('pathways', _('Pathways'), {'urls': 'pathways.urls'}),
))


Pathway.register_extensions(
    'feincms.module.extensions.translations',
)
Pathway.register_regions(
    ('main', _('Main content area')),
)
Pathway.create_content_type(RichTextContent)
Pathway.create_content_type(MediaFileContent, TYPE_CHOICES=(
    ('default', _('default')),
    ('lightbox', _('lightbox')),
))