import os
import sys
from django.utils.translation import gettext_lazy as _

DIRNAME = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG
COMPRESS_ENABLED = False
COMPRESS_CACHE_BACKEND = 'locmem:///'

DEFAULT_FROM_EMAIL = 'your_email@domain.com'

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'lfs.db',                        # Or path to database file if using sqlite3.
        'USER': '',                              # Not used with sqlite3.
        'PASSWORD': '',                          # Not used with sqlite3.
        'HOST': '',                              # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                              # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# media files settings
MEDIA_URL = '/media/'
MEDIA_ROOT = DIRNAME + "/media"

# static files settings
STATIC_URL = '/static/'
STATIC_ROOT = DIRNAME + "/sitestatic"

# Make this unique, and don't share it with anybody.
SECRET_KEY = '+0zsw5n@v7*rhl6r6ufqhoc6jlqq0f-u8c+gh(hjb+_jmg@rh6'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    "django.contrib.redirects.middleware.RedirectFallbackMiddleware",
    "pagination.middleware.PaginationMiddleware",
    "lfs.utils.middleware.AJAXSimpleExceptionResponse",
    "lfs.utils.middleware.ProfileMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'urls'

SESSION_SERIALIZER = "django.contrib.sessions.serializers.PickleSerializer"

INSTALLED_APPS = (
    'lfs_theme',
    'compressor',
    "django.contrib.admin",
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.redirects',
    'django.contrib.sitemaps',
    'django_countries',
    'pagination',
    'reviews',
    'portlets',
    'lfs',
    'lfs.addresses',
    'lfs.caching',
    'lfs.cart',
    'lfs.catalog',
    'lfs.checkout',
    'lfs.core',
    'lfs.criteria',
    'lfs.customer',
    'lfs.customer_tax',
    'lfs.discounts',
    'lfs.export',
    'lfs.gross_price',
    'lfs.mail',
    'lfs.manage',
    'lfs.marketing',
    'lfs.manufacturer',
    'lfs.net_price',
    'lfs.order',
    'lfs.page',
    'lfs.payment',
    'lfs.portlet',
    'lfs.search',
    'lfs.shipping',
    'lfs.supplier',
    'lfs.tax',
    'lfs.tests',
    'lfs.utils',
    'lfs.voucher',
    'lfs_contact',
    'lfs_order_numbers',
    'localflavor',
    'postal',
    'paypal.standard.ipn',
    'south',
    'lfs_criterion_us_states',
    'django_nose',
    'debug_toolbar',
)

FORCE_SCRIPT_NAME = ""

LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/manage/"

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'lfs.core.context_processors.main',
)

AUTHENTICATION_BACKENDS = (
    'lfs.customer.auth.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        'KEY_PREFIX': 'lfs'
    }
}

EMAIL_HOST = ""
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""

PAYPAL_RECEIVER_EMAIL = "info@yourbusiness.com"
PAYPAL_IDENTITY_TOKEN = "set_this_to_your_paypal_pdt_identity_token"

LFS_PAYPAL_REDIRECT = True
LFS_AFTER_ADD_TO_CART = "lfs_added_to_cart"
LFS_RECENT_PRODUCTS_LIMIT = 5

LFS_LOCALE = "en_US.UTF-8"

LFS_ORDER_NUMBER_GENERATOR = "lfs_order_numbers.models.OrderNumberGenerator"
LFS_DOCS = "http://docs.getlfs.com/en/latest/"

LFS_INVOICE_COMPANY_NAME_REQUIRED = False
LFS_INVOICE_EMAIL_REQUIRED = True
LFS_INVOICE_PHONE_REQUIRED = True

LFS_SHIPPING_COMPANY_NAME_REQUIRED = False
LFS_SHIPPING_EMAIL_REQUIRED = False
LFS_SHIPPING_PHONE_REQUIRED = False

LFS_PAYMENT_METHOD_PROCESSORS = [
    ["lfs_paypal.PayPalProcessor", _(u"PayPal")],
]

LFS_PRICE_CALCULATORS = [
    ['lfs.gross_price.GrossPriceCalculator', _(u'Price includes tax')],
    ['lfs.net_price.NetPriceCalculator', _(u'Price excludes tax')],
]

LFS_SHIPPING_METHOD_PRICE_CALCULATORS = [
    ["lfs.shipping.GrossShippingMethodPriceCalculator", _(u'Price includes tax')],
    ["lfs.shipping.NetShippingMethodPriceCalculator", _(u'Price excludes tax')],
]

LFS_UNITS = [
    u"l",
    u"m",
    u"qm",
    u"cm",
    u"lfm",
    u"Package",
    u"Piece",
]

LFS_PRICE_UNITS = LFS_BASE_PRICE_UNITS = LFS_PACKING_UNITS = LFS_UNITS

LFS_CRITERIA = [
    ["lfs.criteria.models.CartPriceCriterion", _(u"Cart Price")],
    ["lfs.criteria.models.CombinedLengthAndGirthCriterion", _(u"Combined Length and Girth")],
    ["lfs.criteria.models.CountryCriterion", _(u"Country")],
    ["lfs.criteria.models.HeightCriterion", _(u"Height")],
    ["lfs.criteria.models.LengthCriterion", _(u"Length")],
    ["lfs.criteria.models.WidthCriterion", _(u"Width")],
    ["lfs.criteria.models.WeightCriterion", _(u"Weight")],
    ["lfs.criteria.models.ShippingMethodCriterion", _(u"Shipping Method")],
    ["lfs.criteria.models.PaymentMethodCriterion", _(u"Payment Method")],
    ["lfs_criterion_us_states.models.USStatesCriterion", _(u"US State")],
]

REVIEWS_SHOW_PREVIEW = False
REVIEWS_IS_NAME_REQUIRED = False
REVIEWS_IS_EMAIL_REQUIRED = False
REVIEWS_IS_MODERATED = False

LOGGING = {
    "version": 1,
    "formatters": {
        "verbose": {
            "format": "%(asctime)s %(levelname)s %(message)s",
            "datefmt": "%a, %d %b %Y %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(DIRNAME, "..", "lfs.log"),
            'mode': 'a',
        },
    },
    "loggers": {
        "default": {
            "handlers": ["logfile", "console"],
            "level": "DEBUG",
            "propagate": False,
        },
    }
}

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = ['--nocapture']

# apps that we want jenkins ci to test
PROJECT_APPS = ['lfs.core']
JENKINS_TASKS = (
    'django_jenkins.tasks.run_pylint',
    #'django_jenkins.tasks.with_coverage',
    'django_jenkins.tasks.django_tests',
    'django_jenkins.tasks.run_pep8',
    'django_jenkins.tasks.run_pyflakes',
    #'django_jenkins.tasks.windmill_tests',
)

PISTON_DISPLAY_ERRORS = True

# disable south logger while running tests to prevent output of huge amount of data
if 'test' in sys.argv:
    LOGGING['loggers']['south'] = dict(level="INFO")

try:
    from local_settings import *
except ImportError:
    pass
