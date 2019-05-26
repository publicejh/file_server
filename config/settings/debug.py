from .common import *

config_secret_debug = json.loads(open(CONFIG_SECRET_DEBUG_FILE).read())

DEBUG = True
ALLOWED_HOSTS = config_secret_debug['django']['allowed_hosts']

# WSGI application
WSGI_APPLICATION = 'config.wsgi.debug.application'

DATABASES = config_secret_debug['django']['databases']

CORS_ORIGIN_ALLOW_ALL = True
