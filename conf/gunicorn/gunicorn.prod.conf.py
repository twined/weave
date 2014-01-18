bind = "unix:/sites/prod/{{ project_name }}/conf/gunicorn/sock/{{ project_name }}-prod.sock"
logfile = "/sites/prod/{{ project_name }}/logs/gunicorn.log"
workers = 3
user = "{{ project_name }}"
proc_name = "{{ project_name }}_prod"
