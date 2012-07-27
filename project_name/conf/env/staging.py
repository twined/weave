from conf.settings import *

DEBUG = False

PIPELINE_YUI_BINARY = "/usr/bin/yui-compressor"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ project_name }}_staging',
        'USER': '{{ project_name }}',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}