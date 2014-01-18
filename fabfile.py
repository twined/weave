#!/usr/bin/env python
import os
from datetime import datetime
from fabric.api import *
from fabric.colors import yellow, blue

from glue.bottle import *
from glue.bottle import _get_version
from glue.settings import GLUE_SETTINGS

print yellow("""
                     M,
                   ,MMMM,_____
                 ,dMMMMMMMMMMMMMMMMb,_
              ,dMMMMMMMMMMMMMMMMMMMMMMMMMMb,_
            ,MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMb
          dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMb,
        ,MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMb,
       dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMb,
      MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM,
     =:~=MMMMMMMMMMM:         =MMMMMMMMMMMMMMMMMMMMMMM,
            ,MMMM,               +MMMMMMMMMMMMMMMMMMMMM
               :                   MMMMMMMMMMMMMMMMMMMM,
                                    :MMMMMMMMMMMMMMMMMMb
                        ___           MMMMMMMMMMMMMMMMMM,
     ~++,            ,dMMMMMb,         'MMMMMMMMMMMMMMMMb
  =+++++++=          :MMMMMMMMb,_         YMMMMMMMMMMMMMMM
  ++++++++++++:        `+YMMMMMMMMb         'MMMMMMMMMMMM:
  +++++++++++++++:         ^MMMMMMMMb         'MMMMMMMMP
  +++++++++++++++++           +MMMMMM,           '~MM+P'
  :+++++++++++++++++:           ~+~
   +++++++++++++++++++
   ,+++++++++++++++++++:
    +++++++++++++++++++++:               ,+++~
     +++++++++++++++++++++++,_       _,++++++++++~: ,:
       `+++++++++++++++++++++++++++++++++++++++++++P
         =+++++++++++++++++++++++++++++++++++++++~`
          ,+++++++++++++++++++++++++++++++++++++
            :+++++++++++++++++++++++++++++++++,
              \"+++++++++++++++++++++++++++++'
                 \"~+++++++++++++++++++++++'
                     '\"+++++++++++++++++'
                                 \,++++:
                                    ++'
                                     '
""")

print "-------------------------------------------------------------"
print blue('& twined deployment script v%s. copyright twined 2010-%s' % (
    _get_version(), datetime.now().year))
print "-------------------------------------------------------------"
print ""


def prod():
    """
    Use the production server
    """
    # the flavor of the django environment
    env.flavor = 'prod'
    # the process name, also the base name
    env.procname = GLUE_SETTINGS['prod']['process_name']

    # username for the ssh connection
    env.user = GLUE_SETTINGS['ssh_user']
    # hostname for the ssh connection
    env.host = GLUE_SETTINGS['ssh_host']
    # port for the ssh connection
    env.port = GLUE_SETTINGS['ssh_port']
    # here we build the hosts string
    env.hosts = ['%s@%s:%s' % (env.user, env.host, env.port)]

    # full path to virtualenvs root
    env.venv_root = GLUE_SETTINGS['prod']['venv_root']
    # virtualenv name
    env.venv_name = GLUE_SETTINGS['prod']['venv_name']
    # full path to the virtualenv we want to create
    env.venv_path = os.path.join(GLUE_SETTINGS['prod']['venv_root'], GLUE_SETTINGS['prod']['venv_name'])
    # the path to clone our git repo into
    env.path = os.path.join(GLUE_SETTINGS['prod']['project_base'], GLUE_SETTINGS['project_name'])
    # name of the repo we are cloning
    env.repo = '%s' % GLUE_SETTINGS['prod']['repo']
    # branch name to clone, or empty for master
    env.branch = GLUE_SETTINGS['prod']['git_branch']

    # the user we will create on host, also runs manage.py tasks etc.
    env.project_user = GLUE_SETTINGS['project_name']
    # the group we add the user to. this is what the project path
    # gets chowned to
    env.project_group = GLUE_SETTINGS['project_group']

    # if enabled, clears the memcached after git pulls
    env.memcached_enabled = GLUE_SETTINGS['prod']['memcached_enabled']
    # not implemented yet
    env.redis_enabled = GLUE_SETTINGS['prod']['redis_enabled']
    env.redis_key = GLUE_SETTINGS['prod']['redis_key']

    # the postgres database username we create
    env.db_user = GLUE_SETTINGS['prod']['db_user']
    # name of the postgres database we create
    env.db_name = GLUE_SETTINGS['prod']['db_name']
    # password to the postgres database user
    env.db_pass = GLUE_SETTINGS['prod']['db_pass']
    # full path to our project's public/ directory
    env.public_path = os.path.join(env.path, GLUE_SETTINGS['prod']['public_path'])
    # full path to our project's media directory
    env.media_path = os.path.join(env.public_path, GLUE_SETTINGS['prod']['media_path'])
    # application name
    env.project_name = GLUE_SETTINGS['project_name']


def staging():
    """
    Use the staging server
    """
    # the flavor of the django environment
    env.flavor = 'staging'
    # the process name, also the base name
    env.procname = GLUE_SETTINGS['staging']['process_name']

    # username for the ssh connection
    env.user = GLUE_SETTINGS['ssh_user']
    # hostname for the ssh connection
    env.host = GLUE_SETTINGS['ssh_host']
    # port for the ssh connection
    env.port = GLUE_SETTINGS['ssh_port']
    # here we build the hosts string
    env.hosts = ['%s@%s:%s' % (env.user, env.host, env.port)]

    # full path to virtualenvs root
    env.venv_root = GLUE_SETTINGS['staging']['venv_root']
    # virtualenv name
    env.venv_name = GLUE_SETTINGS['staging']['venv_name']
    # full path to the virtualenv we want to create
    env.venv_path = os.path.join(GLUE_SETTINGS['staging']['venv_root'], GLUE_SETTINGS['staging']['venv_name'])
    # the path to clone our git repo into
    env.path = os.path.join(GLUE_SETTINGS['staging']['project_base'], GLUE_SETTINGS['project_name'])
    # name of the repo we are cloning
    env.repo = '%s' % GLUE_SETTINGS['staging']['repo']
    # branch name to clone, or empty for master
    env.branch = GLUE_SETTINGS['staging']['git_branch']

    # the user we will create on host, also runs manage.py tasks etc.
    env.project_user = GLUE_SETTINGS['project_name']
    # the group we add the user to. this is what the project path
    # gets chowned to
    env.project_group = GLUE_SETTINGS['project_group']

    # if enabled, clears the memcached after git pulls
    env.memcached_enabled = GLUE_SETTINGS['staging']['memcached_enabled']
    # not implemented yet
    env.redis_enabled = GLUE_SETTINGS['staging']['redis_enabled']
    env.redis_key = GLUE_SETTINGS['staging']['redis_key']

    # the postgres database username we create
    env.db_user = GLUE_SETTINGS['staging']['db_user']
    # name of the postgres database we create
    env.db_name = GLUE_SETTINGS['staging']['db_name']
    # password to the postgres database user
    env.db_pass = GLUE_SETTINGS['staging']['db_pass']
    # full path to our project's public/ directory
    env.public_path = os.path.join(env.path, GLUE_SETTINGS['staging']['public_path'])
    # full path to our project's media directory
    env.media_path = os.path.join(env.public_path, GLUE_SETTINGS['staging']['media_path'])
    # application name
    env.project_name = GLUE_SETTINGS['project_name']
