from oscar.core.loading import get_model

Category = get_model('catalogue', 'Category')
from wagtail.core.models import Page, Site

from demo.models import StandardIndexPage


def create_shop_root():
    site_root_page = Site.objects.first().root_page
    try:
        shop_page = site_root_page.get_children().get(title="Shop")
        print('create_shop_root(): page already existing')
    except Page.DoesNotExist:
        print('create_shop_root(): create page')
        shop_page = StandardIndexPage(
            title="Shop",
            slug="shop",
            #content_type=language_redirection_page_content_type,
            show_in_menus=True
        )
        shop_page = site_root_page.add_child(instance=shop_page)
        shop_page.save()
    return shop_page


def create_from_sequence(bits):
    """
    Create categories from an iterable
    """
    if len(bits) == 1:
        # Get or create root node
        name = bits[0]
        try:
            # Category names should be unique at the depth=2
            root = Category.get_root_nodes().get(title=name)
        except Category.DoesNotExist:
            #root = Category.add_root(title=name)
            shop_page = create_shop_root()
            root = Category(title=name)
            shop_page.add_child(instance=root)
        except Category.MultipleObjectsReturned:
            raise ValueError((
                "There are more than one categories with name "
                "%s at depth=1") % name)
        return [root]
    else:
        parents = create_from_sequence(bits[:-1])
        parent, name = parents[-1], bits[-1]

        try:
            child = parent.get_children().get(title=name)
        except (Page.DoesNotExist, Category.DoesNotExist):
            child = parent.add_child(title=name)
        except Category.MultipleObjectsReturned:
            raise ValueError((
                "There are more than one categories with name "
                "%s which are children of %s") % (name, parent))

        parents.append(child)
        return parents


def create_from_breadcrumbs(breadcrumb_str, separator='>'):
    """
    Create categories from a breadcrumb string
    """
    category_names = [x.strip() for x in breadcrumb_str.split(separator)]
    categories = create_from_sequence(category_names)
    return categories[-1]
