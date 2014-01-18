bind = "unix:/sites/staging/{{ project_name }}/conf/gunicorn/sock/{{ project_name }}-staging.sock"
logfile = "/sites/staging/{{ project_name }}/logs/gunicorn.log"
workers = 3
user = "{{ project_name }}"
proc_name = "{{ project_name }}_staging"
