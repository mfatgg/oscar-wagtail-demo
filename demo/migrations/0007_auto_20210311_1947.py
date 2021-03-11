# Generated by Django 2.0.13 on 2021-03-11 19:47

import catalogue.blocks
import demo.models
from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0006_auto_20210303_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.StreamField([('h2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('aligned_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.RichTextBlock()), ('alignment', demo.models.ImageFormatChoiceBlock())], icon='image', label='Aligned image')), ('pullquote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.TextBlock('quote title')), ('attribution', wagtail.core.blocks.CharBlock())])), ('aligned_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', demo.models.HTMLAlignmentChoiceBlock())], icon='code', label='Raw HTML')), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('productlist', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('subtitle', wagtail.core.blocks.CharBlock()), ('products', wagtail.core.blocks.ListBlock(catalogue.blocks.ProductChooserBlock))], label='Product List')), ('singleproduct', catalogue.blocks.ProductChooserBlock(label='Single Product'))]),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('h2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('aligned_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.RichTextBlock()), ('alignment', demo.models.ImageFormatChoiceBlock())], icon='image', label='Aligned image')), ('pullquote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.TextBlock('quote title')), ('attribution', wagtail.core.blocks.CharBlock())])), ('aligned_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', demo.models.HTMLAlignmentChoiceBlock())], icon='code', label='Raw HTML')), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('productlist', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('subtitle', wagtail.core.blocks.CharBlock()), ('products', wagtail.core.blocks.ListBlock(catalogue.blocks.ProductChooserBlock))], label='Product List')), ('singleproduct', catalogue.blocks.ProductChooserBlock(label='Single Product'))]),
        ),
    ]