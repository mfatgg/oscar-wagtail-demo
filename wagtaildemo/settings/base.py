# Django settings for oscar-wagtail-demo project

import os

from django.utils.translation import ugettext_lazy as _
from oscar.defaults import *  # noqa

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), '..', '..')
BASE_DIR = PROJECT_ROOT

DEBUG = True

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

# Default to dummy email backend. Configure dev/production/local backend
# as per https://docs.djangoproject.com/en/dev/topics/email/#email-backends
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'oscarwagtaildemo',
    }
}
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

DATE_FORMAT = 'j F Y'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)

# ** You would never normally put the SECRET_KEY in a public repository,
# ** however this is a demo app so we're using the default settings.
# ** Don't use this key in any non-demo usage!
# Make this unique, and don't share it with anybody.
SECRET_KEY = 'wq21wtjo3@d_qfjvd-#td!%7gfy2updj2z+nev^k$iy%=m4_tr'

MIDDLEWARE = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',

    'oscar.apps.basket.middleware.BasketMiddleware',

    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'wagtaildemo.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wagtaildemo.wsgi.application'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    # 'django.contrib.sites',  # Wagtail uses its own site management logic
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',

    'compressor',
    'widget_tweaks',
    'taggit',
    'modelcluster',
    'rest_framework',
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'wagtail.core',
    'wagtail.admin',
    'wagtail.documents',
    'wagtail.snippets',
    'wagtail.users',
    'wagtail.images',
    'wagtail.embeds',
    'wagtail.search',
    'wagtail.contrib.redirects',
    'wagtail.contrib.forms',
    'wagtail.sites',
    #'wagtail.contrib.wagtailapi',

    'django_tables2',
    'haystack',
    'sorl.thumbnail',
    #'oscar',
    'wagtaildemo',
    'oscar.apps',
    'oscar.apps.address',
    'oscar.apps.analytics',
    'oscar.apps.basket',
    #'oscar.apps.catalogue',
    'demo.apps.catalogue',
    'oscar.apps.catalogue.reviews',
    'oscar.apps.checkout',
    'oscar.apps.customer',
    'oscar.apps.offer',
    'oscar.apps.order',
    #'oscar.apps.partner',
    'demo.apps.partner',
    'oscar.apps.payment',
    'oscar.apps.search',
    'oscar.apps.shipping',
    'oscar.apps.voucher',
    'oscar.apps.wishlists',
    'oscar_promotions.apps.PromotionsConfig',
    'oscar.apps.dashboard',
    #'oscar.apps.dashboard.catalogue',
    'demo.apps.dashboard.catalogue',
    'oscar.apps.dashboard.communications',
    'oscar.apps.dashboard.offers',
    'oscar.apps.dashboard.orders',
    'oscar.apps.dashboard.pages',
    'oscar.apps.dashboard.partners',
    'oscar.apps.dashboard.ranges',
    'oscar.apps.dashboard.reports',
    'oscar.apps.dashboard.reviews',
    'oscar.apps.dashboard.shipping',
    'oscar.apps.dashboard.users',
    'oscar.apps.dashboard.vouchers',
    'oscar_promotions.dashboard.apps.PromotionsDashboardConfig',
    'demo',
]


HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

# Add wagtail.contrib.searchpromotions to INSTALLED_APPS
# if we're on Wagtail 1.1 or later.
# NB this is a quick-and-dirty version check that won't work with
# full generality (double-digit versions, alpha/beta releases)
from wagtail.core import __version__  # noqa
if __version__.split('.') > ['2', '0']:
    INSTALLED_APPS = list(INSTALLED_APPS) + [
        'wagtail.contrib.search_promotions'
    ]
elif __version__.split('.') > ['1', '0']:
    INSTALLED_APPS = list(INSTALLED_APPS) + [
        'wagtail.contrib.searchpromotions'
    ]


EMAIL_SUBJECT_PREFIX = '[wagtaildemo] '

INTERNAL_IPS = ('127.0.0.1', '10.0.2.2')


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.contrib.messages.context_processors.messages',

                'oscar.apps.search.context_processors.search_form',
                'oscar_promotions.context_processors.promotions',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.customer.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',
            ],
        },
    },
]

# django-compressor settings
COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


# WAGTAIL SETTINGS

WAGTAIL_SITE_NAME = 'oscar-wagtail-demo'


# OSCAR SETTINGS

OSCAR_DASHBOARD_NAVIGATION = [
    {
        'label': _('Wagtail CMS'),
        'icon': 'icon-book',
        'url_name': 'wagtailadmin_home',
        'access_fn': lambda user, url_name, url_args, url_kwargs: user.is_staff
    },
] + OSCAR_DASHBOARD_NAVIGATION  # noqa

OSCAR_DASHBOARD_NAVIGATION[5]['children'] += [
    {
        'label': 'Content blocks',
        'url_name': 'oscar_promotions_dashboard:promotion-list',
    },
    {
        'label': 'Content blocks by page',
        'url_name': 'oscar_promotions_dashboard:promotion-list-by-page',
    },
]
