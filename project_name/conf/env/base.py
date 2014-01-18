# -*- coding: utf-8 -*-

import os
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read(os.path.join(os.path.split(__file__)[0], 'secrets.cfg'))

# Make this unique, and don't share it with anybody.
SECRET_KEY = config.get('BASE', 'SECRET_KEY')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

SERVE_STATIC_LOCALLY = False

# ------------------------------------------------
# Admin config
# ------------------------------------------------

ADMIN_CONFIG = {
    'site_name': '{{ project_name }}',
    'site_url': '{{ project_name }}',
}

# ------------------------------------------------
# TWYTHON
# ------------------------------------------------

TWYTHON = {
    'app_key': config.get('BASE', 'TWYTHON_APP_KEY'),
    'app_secret': config.get('BASE', 'TWYTHON_APP_SECRET'),
    'oauth_token': config.get('BASE', 'TWYTHON_OAUTH_TOKEN'),
    'oauth_token_secret': config.get('BASE', 'TWYTHON_OAUTH_TOKEN_SECRET'),
}

# ------------------------------------------------
# glue
# ------------------------------------------------

GLUE_SETTINGS = {
    'ssh_user': 'trond',
    'ssh_host': 'twined.net',
    'ssh_port': 30000,
    'prod': {
        'process_name': '{{ project_name }}_prod',
        'repo': '{{ project_name }}',
        'git_branch': 'master',
        'db_user': '{{ project_name }}',
        'db_pass': config.get('PROD', 'DB_PASS'),
    },
    'staging': {
        'repo': '{{ project_name }}',
        'git_branch': 'master',
        'db_user': '{{ project_name }}',
        'db_pass': config.get('STAGING', 'DB_PASS'),
    }
}

# -----------------------------------------------
# analytics
# -----------------------------------------------

GOOGLE_ANALYTICS_APP_NAME = config.get('BASE',
                                       'GOOGLE_ANALYTICS_APP_NAME')
GOOGLE_ANALYTICS_TABLE_ID = config.get('BASE',
                                       'GOOGLE_ANALYTICS_TABLE_ID')
GOOGLE_ANALYTICS_LOGIN = config.get('BASE',
                                    'GOOGLE_ANALYTICS_LOGIN')
GOOGLE_ANALYTICS_PASSWORD = config.get('BASE',
                                       'GOOGLE_ANALYTICS_PASSWORD')
