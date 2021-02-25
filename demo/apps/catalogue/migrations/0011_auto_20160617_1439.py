# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import demo.apps.catalogue.blocks
import wagtail.images.blocks
import wagtail.core.fields
import wagtail.core.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0013_make_rendition_upload_callable'),
        ('catalogue', '0010_auto_20160616_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('product_block', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('subtitle', wagtail.core.blocks.CharBlock()), ('products', wagtail.core.blocks.ListBlock(demo.apps.catalogue.blocks.ProductChooserBlock))]))], default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(verbose_name='Description', blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name', db_index=True),
        ),
    ]
