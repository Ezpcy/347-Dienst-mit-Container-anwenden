#!/bin/sh
envsubst '$BACKEND_HOST' </etc/nginx/conf.d/custom-nginx.template >/etc/nginx/conf.d/default.conf
/docker-entrypoint.d/env.sh
exec nginx -g "daemon off;"
