{% if False %}
WEAVE
=====

Installation instructions:

    - Create your working environment and virtualenv
    - Install Django ($ pip install Django)
    - $ django-admin.py startproject --template https://github.com/twined/weave/zipball/master --extension py,md,rst,txt,conf,bash_profile_source,cfg projectname
    - $ cd projectname
    - $ chmod +x manage.py
    - $ pip install -r requirements/dev.pip

{% endif %}

# {{ project_name|title }} Django Project