from django import forms
from django.utils.functional import cached_property
from oscar.core.loading import get_model

from wagtail.core import blocks


class ProductChooserBlock(blocks.ChooserBlock):
    @cached_property
    def target_model(self):
        return get_model('catalogue', 'product')

    widget = forms.Select

    class Meta:
        app_label = 'catalogue'

    def value_for_form(self, value):
        # return the key value for the select field
        if isinstance(value, self.target_model):
            return value.pk
        else:
            return value


class ProductBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    subtitle = blocks.CharBlock()
    products = blocks.ListBlock(ProductChooserBlock)
