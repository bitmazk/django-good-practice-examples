"""Settings that need to be set in order to run the tests."""
import os

DEBUG = True
FILER_DEBUG = True

SITE_ID = 1

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

USE_I18N = True

LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('en', 'English'),
    ('de', 'German'),
)

ROOT_URLCONF = 'good_practice_examples.tests.urls'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(os.path.dirname(__file__), '../../static/')
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), '../../media/')

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), 'test_static'),
)

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), '../templates'),
)

COVERAGE_REPORT_HTML_OUTPUT_DIR = os.path.join(
    os.path.dirname(__file__), 'coverage')

COVERAGE_MODULE_EXCLUDES = [
    'tests$', 'settings$', 'urls$', 'locale$',
    'migrations', 'fixtures', 'admin$', 'django_extensions',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'simple_translation.middleware.MultilingualGenericsMiddleware',
]

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
)

EXTERNAL_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django_nose',
    'cms',
    'mptt',
    'simple_translation',
]

INTERNAL_APPS = [
    'good_practice_examples',
]


SECRET_KEY = 'this is no real secret key'

INSTALLED_APPS = EXTERNAL_APPS + INTERNAL_APPS

COVERAGE_MODULE_EXCLUDES += EXTERNAL_APPS

CMS_SOFTROOT = True
CMS_PERMISSION = False
CMS_SEO_FIELDS = True
CMS_MENU_TITLE_OVERWRITE = True
CMS_FRONTEND_LANGUAGES = ('en', 'de', )
CMS_TEMPLATES = (
    ('standard.html', 'Standard'),
)
