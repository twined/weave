import os
import ConfigParser

from {{ project_name }}.conf.settings import *

config = ConfigParser.RawConfigParser()
config.read(os.path.join(os.path.split(__file__)[0], 'secrets.cfg'))

DEBUG = True

HIVER_SETTINGS = {
    'disabled': True,
    'cache_duration': 60 * 60 * 12,
}

LOCKDOWN_PASSWORDS = ('lockdown',)

MIDDLEWARE_CLASSES += (
    'lockdown.middleware.LockdownMiddleware',
)

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

PIPELINE_YUI_BINARY = "/usr/bin/yui-compressor"
PIPELINE_YUGLIFY_BINARY = \
    '/sites/.virtualenvs/{{ project_name }}_prod/node_modules/yuglify/bin/yuglify'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ project_name }}_staging',
        'USER': '{{ project_name }}',
        'PASSWORD': config.get('STAGING', 'DB_PASS'),
        'HOST': '',
        'PORT': '',
    }
}
