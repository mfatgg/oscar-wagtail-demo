from django.utils.translation import gettext_lazy as _

from oscar.apps.offer.abstract_models import AbstractRange
from oscar.core.loading import get_model
from modelcluster import fields


class Range(AbstractRange):
    included_categories = fields.ParentalManyToManyField(
        'catalogue.Category', related_name='includes', blank=True,
        verbose_name=_("Included Categories"))


from oscar.apps.offer.models import *  # noqa isort:skip
