# Global settings for {{ project_name }} project.
import os
import sys

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PROJECT_BASE = os.path.join(PROJECT_PATH, "..")
PUBLIC_PATH = os.path.join(PROJECT_BASE, 'public')

# use apps/ directory
sys.path.insert(0, os.path.join(PROJECT_PATH, "apps"))


DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
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

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = '{{ secret_key }}'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PUBLIC_PATH, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PUBLIC_PATH, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make the messages twitter-bootstrap-friendly.
from django.contrib.messages import constants as message_constants

MESSAGE_TAGS = {
    message_constants.DEBUG: 'alert-debug',
    message_constants.INFO: 'alert-info',
    message_constants.SUCCESS: 'alert-success',
    message_constants.WARNING: 'alert-warning',
    message_constants.ERROR: 'alert-error',
}

# cache config
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': 'localhost:6379',
        'OPTIONS': {
            'DB': 'CHANGE_ME',
            'PARSER_CLASS': 'redis.connection.HiredisParser',
        },
        'KEY_PREFIX': '{{ project_name }}',
    },
}

from django.core.urlresolvers import reverse_lazy

LOGIN_REDIRECT_URL = reverse_lazy('admin:dashboard')
LOGIN_URL = '/admin/login/'
LOGOUT_URL = '/admin/logout/'

# sorl thumbnails
THUMBNAIL_DEBUG = DEBUG
THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'

# Crispy forms config
CRISPY_TEMPLATE_PACK = 'bootstrap'
CRISPY_FAIL_SILENTLY = not DEBUG

# Pipeline config
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

PIPELINE_CSS = {
    'app': {
        'source_filenames': (
          'css/{{ project_name }}.css',
          'css/{{ project_name }}-responsive.css',
          'css/lightbox.css',
        ),
        'output_filename': 'css/app.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
    'admin': {
        'source_filenames': (
          'css/{{ project_name }}-admin.css',
        ),
        'output_filename': 'css/admin.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}

PIPELINE_JS = {
    'app': {
        'source_filenames': (
            'js/libs/bootstrap/bootstrap-transition.js',
            'js/libs/bootstrap/bootstrap-alert.js',
            #'js/libs/bootstrap/bootstrap-modal.js',
            #'js/libs/bootstrap/bootstrap-dropdown.js',
            #'js/libs/bootstrap/bootstrap-scrollspy.js',
            #'js/libs/bootstrap/bootstrap-tab.js',
            'js/libs/bootstrap/bootstrap-tooltip.js',
            'js/libs/bootstrap/bootstrap-popover.js',
            #'js/libs/bootstrap/bootstrap-button.js',
            #'js/libs/bootstrap/bootstrap-collapse.js',
            'js/libs/bootstrap/bootstrap-carousel.js',
            #'js/libs/bootstrap/bootstrap-typeahead.js',
            'js/libs/waypoints/waypoints.min.js',
            'js/libs/lightbox/lightbox.js',
            'js/{{ project_name }}.js',
        ),
        'output_filename': 'js/app.js',
    },
    'admin': {
        'source_filenames': (
            'js/libs/jquery/jquery.js',
            'js/libs/jquery/jquery.slugit.js',
            'js/libs/jquery/jquery.debounce-1.0.5.js'
            'js/libs/bootstrap/bootstrap-transition.js',
            'js/libs/bootstrap/bootstrap-alert.js',
            'js/libs/bootstrap/bootstrap-modal.js',
            'js/libs/bootstrap/bootstrap-dropdown.js',
            'js/libs/bootstrap/bootstrap-scrollspy.js',
            'js/libs/bootstrap/bootstrap-tab.js',
            'js/libs/bootstrap/bootstrap-tooltip.js',
            'js/libs/bootstrap/bootstrap-popover.js',
            'js/libs/bootstrap/bootstrap-button.js',
            'js/libs/bootstrap/bootstrap-collapse.js',
            'js/libs/bootstrap/bootstrap-carousel.js',
            'js/libs/bootstrap/bootstrap-typeahead.js',
        ),
        'output_filename': 'js/admin.js',
    }
}

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    #'django.middleware.gzip.GZipMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = '{{ project_name }}.conf.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
)

FIXTURE_DIRS = (
    os.path.join(PROJECT_PATH, 'fixtures'),
)

INTERNAL_IPS = ('127.0.0.1', '0.0.0.0', '10.0.2.2',)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'crispy_forms',
    'debug_toolbar',
    'pipeline',
    'sorl.thumbnail',
    'south',

    'application',
    'hiver',
    'posts',
    'pages',
    'admin',
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

# ------------
# -- FLAVOR --
# ------------

FLAVOR = os.environ.get('FLAVOR', 'dev')


def override_settings(dottedpath):
    try:
        _m = __import__(dottedpath, fromlist=[None])
    except ImportError:
        pass
    else:
        _thismodule = sys.modules[__name__]
    for _k in dir(_m):
        setattr(_thismodule, _k, getattr(_m, _k))

override_settings('{{ project_name }}.conf.env.' + FLAVOR)
