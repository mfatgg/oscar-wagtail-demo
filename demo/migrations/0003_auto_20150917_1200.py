# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import demo.models
import wagtail.documents.blocks
import wagtail.images.blocks
import wagtail.core.fields
import wagtail.core.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20150917_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.StreamField([('h2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('aligned_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.RichTextBlock()), ('alignment', demo.models.ImageFormatChoiceBlock())], icon='image', label='Aligned image')), ('pullquote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.TextBlock('quote title')), ('attribution', wagtail.core.blocks.CharBlock())])), ('aligned_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', demo.models.HTMLAlignmentChoiceBlock())], label='Raw HTML', icon='code')), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse'))]),
        )
    ]
