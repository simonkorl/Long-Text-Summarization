#!/bin/bash

gunicorn backend.wsgi:application \
--bind 0.0.0.0:8080 \
--workers 2 \
--timeout 30 \
--access-logfile ./logs/access.log \
--error-logfile ./logs/error.log
# --daemon \
