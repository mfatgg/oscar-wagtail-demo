from django.apps import apps
from django.conf.urls import url

from oscar import config


class OscarApplication(config.Shop):

    def get_urls(self):
        """
        Override the default get_urls() method to move default Oscar promotions
        from location r'' to r'^promotions/' to free up space for Wagtail's
        core serving mechanism.
        """
        urlpattern = super(OscarApplication, self).get_urls()[1:]
        urlpattern.append(url(r'^promotions/', apps.get_app_config("oscar_promotions").urls))
        urlpattern.append(url(r'^dashboard/promotions/', apps.get_app_config("oscar_promotions_dashboard").urls))
        return urlpattern
