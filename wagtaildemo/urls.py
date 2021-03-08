from django.apps import apps
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from oscar.core.loading import get_model

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls
#from wagtail.contrib.wagtailapi import urls as wagtailapi_urls

from demo import views


urlpatterns = [
    path('django-admin/', admin.site.urls),

    path('admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),

    re_path(r'search/$', views.search, name='search'),
    #url(r'^api/', include(wagtailapi_urls)),

    # For anything not caught by a more specific rule above, hand over to
    # Oscar's then Wagtail's serving mechanism
    path('', include(apps.get_app_config('oscar').urls[0])),
    path('', include(wagtail_urls)),
]


if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.views.generic.base import RedirectView

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += [
        re_path(r'^favicon\.ico$', RedirectView.as_view(
               url=settings.STATIC_URL + 'demo/images/favicon.ico')
            )
    ]
