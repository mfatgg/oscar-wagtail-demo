from django.db import models
from django.core.cache import cache
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.utils.translation import get_language
from django.utils.translation import ugettext_lazy as _

from oscar.core.utils import slugify
from oscar.core.loading import get_model
from oscar.apps.catalogue.abstract_models import AbstractProductCategory, AbstractProduct
from modelcluster import fields
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock

from catalogue.blocks import ProductBlock


class ProductCategory(AbstractProductCategory):
    category = fields.ParentalKey(
        'catalogue.Category',
        on_delete=models.CASCADE,
        verbose_name=_("Category"))


class Product(AbstractProduct):
    categories = fields.ParentalManyToManyField(
        'catalogue.Category', through='ProductCategory',
        verbose_name=_("Categories"))


class Category(Page):
    """
    The Oscars Category as a Wagtail Page
    This works because they both use Treebeard
    """
    template = "demo/catalogue/cataloguepage.html"
    name = models.CharField(_('Name'), max_length=255, db_index=True)
    description = models.TextField(_('Description'), blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('product_block', ProductBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('description', classname='full'),
        ImageChooserPanel('image'),
        StreamFieldPanel('body'),
    ]

    _slug_separator = '/'
    _full_name_separator = ' > '

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        """
        Returns a string representation of the category and it's ancestors,
        e.g. 'Books > Non-fiction > Essential programming'.

        It's rarely used in Oscar, but used to be stored as a CharField and is
        hence kept for backwards compatibility. It's also sufficiently useful
        to keep around.
        """
        names = [category.title for category in self.get_ancestors_and_self()]
        return self._full_name_separator.join(names)

    @classmethod
    def add_root(cls, **kwargs):
        """
        Adds a Catalogue page node to Wagtail's tree root node. Note that this
        isn't at depth=1 as that's Wagtail's root.
        """
        node = Category.objects.filter(depth=1).first()
        return node.add_child(**kwargs)

    @classmethod
    def get_root_nodes(cls):
        """
        :returns: A queryset containing the root nodes in the tree. This
        differs from the default implementation to find category page root
        nodes by `content_type`.
        """
        content_type = ContentType.objects.get_for_model(cls)
        depth = (cls.objects.filter(content_type=content_type).aggregate(
            depth=models.Min('depth')))['depth']

        if depth is not None:
            return cls.objects.filter(content_type=content_type, depth=depth)

        return cls.objects.filter(content_type=content_type)

    def get_full_slug(self, parent_slug=None):
        if self.is_root():
            return self.slug

        cache_key = self.get_url_cache_key()
        full_slug = cache.get(cache_key)
        if full_slug is None:
            if parent_slug is None:
                full_slug = self.full_slug
            else:
                full_slug = "%s%s%s" % (parent_slug, self._slug_separator, self.slug)
            cache.set(cache_key, full_slug)

        print(f'get_full_slug={full_slug}')

        return full_slug

    @property
    def full_slug(self):
        """
        Returns a string of this category's slug concatenated with the slugs
        of it's ancestors, e.g. 'books/non-fiction/essential-programming'.

        Oscar used to store this as in the 'slug' model field, but this field
        has been re-purposed to only store this category's slug and to not
        include it's ancestors' slugs.
        """
        slugs = [category.slug for category in self.get_ancestors_and_self()]
        fullslug = self._slug_separator.join(slugs)
        print(f'full_slug={fullslug}')
        return fullslug

    def generate_slug(self):
        """
        Generates a slug for a category. This makes no attempt at generating
        a unique slug.
        """
        return slugify(self.name)

    def get_ancestors_and_self(self):
        if self.is_root():
            return [self]

        return list(self.get_ancestors()) + [self]

    def get_descendants_and_self(self):
        """
        Gets descendants and includes itself. Use treebeard's get_descendants
        if you don't want to include the category itself. It's a separate
        function as it's commonly used in templates.
        """
        if self.is_root():
            return [self]

        return list(self.get_descendants()) + [self]
        #return self.get_tree(self)

    @classmethod
    def get_tree(cls, parent=None):
        return cls.objects.all()

    def get_url_cache_key(self):
        current_locale = get_language()
        cache_key = 'CATEGORY_URL_%s_%s' % (current_locale, self.pk)
        return cache_key

    def _get_absolute_url(self, parental_slug=None):
        absolute_url = reverse('catalogue:category', kwargs={
            'category_slug': self.get_full_slug(parent_slug=parental_slug), 'pk': self.pk
        })
        print(f'_get_absolute_url={absolute_url}  pk={self.pk}  id={self.id}  pageptr={self.page_ptr.id}')
        return absolute_url
        #return self.url

    def get_absolute_url(self):
        print('get_absolute_url()')
        return self._get_absolute_url()

    @staticmethod
    def get_search_handler(*args, **kwargs):
        from oscar.apps.catalogue.search_handlers import (
            get_product_search_handler_class
        )
        return get_product_search_handler_class()(*args, **kwargs)

    def get_context(self, request, *args, **kwargs):
        self.search_handler = self.get_search_handler(
            request.GET, request.get_full_path(), self.get_descendants_and_self())
        context = super().get_context(request, *args, **kwargs)
        context['category'] = self
        search_context = self.search_handler.get_search_context_data(
            'products'
        )
        print(f'get_context(): category={self}')
        context.update(search_context)
        return context

    def ensure_slug_uniqueness(self):
        """
        Ensures that the category's slug is unique amongst it's siblings.
        This is inefficient and probably not thread-safe.
        """
        unique_slug = self.slug
        siblings = self.get_siblings().exclude(pk=self.pk)
        next_num = 2
        while siblings.filter(slug=unique_slug).exists():
            unique_slug = '{slug}_{end}'.format(slug=self.slug, end=next_num)
            next_num += 1

        if unique_slug != self.slug:
            self.slug = unique_slug
            self.save()

    def save(self, *args, **kwargs):
        """
        Oscar traditionally auto-generated slugs from names. As that is
        often convenient, we still do so if `slug` is not supplied through
        other means. Also, Wagtail's Page requires `title` where Oscar requires
        `name`. Therefore we set `title` as `name` if `name` but no `title`
         supplied, else set `name` as `title`.
        """

        # Set title and name
        if self.name and not self.title:
            self.title = self.name
        else:
            self.name = self.title

        # Set slug if not supplied
        if self.slug:
            super().save(*args, **kwargs)
        else:
            self.slug = self.generate_slug()
            super().save(*args, **kwargs)
            # We auto-generated a slug, so we need to make sure that it's
            # unique. As we need to be able to inspect the category's siblings
            # for that, we need to wait until the instance is saved. We
            # update the slug and save again if necessary.
            self.ensure_slug_uniqueness()


from oscar.apps.catalogue.models import *  # noqa isort:skip
