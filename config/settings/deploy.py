from .common import *

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

DEBUG = False
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']

# WSGI application
WSGI_APPLICATION = 'config.wsgi.deploy.application'

DATABASES = config_secret_deploy['django']['databases']

CORS_ORIGIN_WHITELIST = [
]

# 각 media 파일에 대한 URL Prefix, 항상 / 로 끝나도록 설정
MEDIA_URL = config_secret_deploy['django']['media_url']

# 업로드된 파일을 저장할 디렉토리 경로
MEDIA_ROOT = os.path.join(BASE_DIR, config_secret_deploy['django']['media_root'])

AUTH_SERVER_TOKEN_VALIDATION_URL = config_secret_deploy['django']['auth_server_token_validation_url']
