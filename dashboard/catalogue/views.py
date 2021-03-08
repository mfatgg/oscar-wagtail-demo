from oscar.apps.dashboard.catalogue import views as orig
from catalogue.models import Category


class CategoryListView(orig.CategoryListView):

    def get_queryset(self):
        return Category.objects.all()
