from {{ project_name }}.conf.settings import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '{{ project_name }}.db',
    }
}

HIVER_SETTINGS = {
    'disabled': True,
}

ALLOWED_HOSTS += ['10.0.81.50']
SERVE_STATIC_LOCALLY = True
PIPELINE = False
