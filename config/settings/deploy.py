from .common import *

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

DEBUG = False
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']

# WSGI application
WSGI_APPLICATION = 'config.wsgi.deploy.application'

DATABASES = config_secret_deploy['django']['databases']

CORS_ORIGIN_WHITELIST = [
]
