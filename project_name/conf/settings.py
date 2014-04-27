# ------------------------------------------------
# core settings
# ------------------------------------------------

import os
import sys

from django.core.urlresolvers import reverse_lazy
from django.contrib.messages import constants as message_constants


# ------------------------------------------------
# utility functions
# ------------------------------------------------

base_path = lambda *x: os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..', *x))
project_path = lambda *x: os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', *x))


# ------------------------------------------------
# use apps/ structure
# ------------------------------------------------

sys.path.insert(0, project_path('apps'))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Admin name', 'admin@email'),
)

SERVER_EMAIL = 'app@email'

MANAGERS = ADMINS

ALLOWED_HOSTS = ['{{ project_name }}.com', '.{{ project_name }}.clients.twined.net']

FEED_TITLE = '{{ project_name }}'

SOUTH_MIGRATION_MODULES = {
    'taggit': 'taggit.south_migrations',
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Oslo'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = base_path('public', 'media')

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = base_path('public', 'static')

# Additional locations of static files
STATICFILES_DIRS = (
    project_path('static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = '{{ project_name }}.conf.urls'

TEMPLATE_DIRS = (
    project_path('templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'cerebrum.context_processors.admin',
)

# ------------------------------------------------
# core cache config / redis
# ------------------------------------------------

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': 'localhost:6379:0',
        'OPTIONS': {
            'PARSER_CLASS': 'redis.connection.HiredisParser',
        },
        'KEY_PREFIX': '{{ project_name }}',
    },
}


# ------------------------------------------------
# hiver cache
# ------------------------------------------------

HIVER_SETTINGS = {
    'disabled': False,
    'cache_duration': 60 * 60 * 12,
}

LOGIN_REDIRECT_URL = reverse_lazy('admin:dashboard')
LOGIN_URL = '/admin/login/'
LOGOUT_URL = '/admin/logout/'


# ------------------------------------------------
# sorl thumbnails
# ------------------------------------------------

THUMBNAIL_DEBUG = DEBUG
THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'

# ------------------------------------------------
# debug toolbar
# ------------------------------------------------

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}


# ------------------------------------------------
# crispy forms
# ------------------------------------------------

CRISPY_TEMPLATE_PACK = 'bootstrap3'
CRISPY_FAIL_SILENTLY = not DEBUG

# ------------------------------------------------
# django-front
# ------------------------------------------------

DJANGO_FRONT_EDITOR_OPTIONS = {
    'customConfig': '/static/js/ckeditor-config.js',
}

# ------------------------------------------------
# imgin config
# ------------------------------------------------

IMGIN_CONFIG = {
    'base': {},
    'postimage': {
        'allowed_exts': [".jpg", ".png", ".jpeg",
                         ".JPG", ".PNG", ".JPEG"],
        'upload_dir': os.path.join('images', 'posts'),
        'size_limit': 10240000,
        'size_map': {
            'l': {
                'landscape': '700',
                'portrait': '700',
                'dir': 'l',
                'class_name': 'large',
                'crop': '',
                'quality': 90,
                'format': 'JPEG',
            },
            'm': {
                'landscape': '310',
                'portrait': '310',
                'dir': 'm',
                'class_name': 'medium',
                'crop': '',
                'quality': 90,
                'format': 'JPEG',
            },
            's': {
                'landscape': '200',
                'portrait': '200',
                'dir': 's',
                'class_name': 'small',
                'crop': '',
                'quality': 90,
                'format': 'JPEG',
            },
            't': {
                'landscape': '140x140',
                'portrait': '140x140',
                'dir': 't',
                'class_name': 'thumb',
                'crop': 'center',
                'quality': 90,
                'format': 'JPEG',
            },
        },
    },
    'portfolio': {
        'allowed_exts': [".jpg", ".png", ".jpeg",
                         ".JPG", ".PNG", ".JPEG"],
        'belongs_to': 'ImageSeries',
        'upload_dir': os.path.join('images', 'portfolio'),
        'size_limit': 5000000,
        'size_map': {
            'l': {
                'landscape': '940',
                'portrait': '880',
                'dir': 'l',
                'class_name': 'large',
                'crop': '',
                'quality': 90,
                'format': 'JPEG',
            },
            'm': {
                'landscape': '310',
                'portrait': '310',
                'dir': 'm',
                'class_name': 'medium',
                'crop': '',
                'quality': 90,
                'format': 'JPEG',
            },
            's': {
                'landscape': '235',
                'portrait': '235',
                'dir': 's',
                'class_name': 'small',
                'crop': '',
                'quality': 90,
                'format': 'JPEG',
            },
            't': {
                'landscape': '140x140',
                'portrait': '140x140',
                'dir': 't',
                'class_name': 'thumb',
                'crop': 'center',
                'quality': 90,
                'format': 'JPEG',
            },
        },
    },
}

# ------------------------------------------------
# pipeline assets configuration
# ------------------------------------------------

PIPELINE = not DEBUG
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yuglify.YuglifyCompressor'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.yuglify.YuglifyCompressor'
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
PIPELINE_CSS = {
    'app': {
        'source_filenames': (
            'css/bootstrap.css',
            'css/application.css',
        ),
        'output_filename': 'css/app.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    }
}

PIPELINE_YUI_BINARY = '/usr/bin/yui-compressor'
PIPELINE_JS = {
    'app': {
        'source_filenames': (
            'js/libs/bootstrap/bootstrap.js',
            'js/libs/prefixfree/prefixfree.min.js',
            'js/{{ project_name }}.js',
        ),
        'output_filename': 'js/app.js',
    }
}


# ------------------------------------------------
# django messages classes
# ------------------------------------------------

MESSAGE_TAGS = {
    message_constants.DEBUG: 'alert-debug',
    message_constants.INFO: 'alert-info',
    message_constants.SUCCESS: 'alert-success',
    message_constants.WARNING: 'alert-warning',
    message_constants.ERROR: 'alert-error',
}


# ------------------------------------------------
# test settings
# ------------------------------------------------

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [
    '--with-coverage', '--cover-html',
    '--cover-html-dir=__coverage',
    '--cover-package=./{{ project_name }}',
    '--cover-erase',
    '--failed', '--stop']

INTERNAL_IPS = ('127.0.0.1', '0.0.0.0', '10.0.2.2',)


# ------------------------------------------------
# Installed Applications
# ------------------------------------------------

# CONTRIB DJANGO APPS
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

# TWINED APPS
INSTALLED_APPS += (
    'cerebrum',
    'imgin',
    'minions',
    'oculus',
    'papermill',
)


# 3RD PARTY APPS
INSTALLED_APPS += (
    'crispy_forms',
    'debug_toolbar',
    'django_extensions',
    'pipeline',
    'sorl.thumbnail',
    'south',
    'taggit',
    'lockdown',
    'front',
)


# ------------------------------------------------
# Logging
# ------------------------------------------------

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },

    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },

    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            #'formatter': 'simple'
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(base_path('logs'),
                                     'application_error.log'),
            'formatter': 'verbose',
        },
    },

    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'logfile'],
            'level': 'ERROR',
            'propagate': True,
        },
        'envelope.forms': {
            'handlers': ['logfile'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}

try:
    from {{ project_name }}.conf.env.base import *
except ImportError:
    pass

# ------------------------------------------------
# flavor
# ------------------------------------------------

FLAVOR = os.environ.get('FLAVOR', 'dev')
SETTINGS_ENV_DOTTEDPATH = '{{ project_name }}.conf.env.'


def override_settings(dottedpath):
    try:
        _m = __import__(dottedpath, fromlist=[None])
    except ImportError:
        pass
    else:
        _thismodule = sys.modules[__name__]
    for _k in dir(_m):
        setattr(_thismodule, _k, getattr(_m, _k))

override_settings(SETTINGS_ENV_DOTTEDPATH + FLAVOR)
