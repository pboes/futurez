from conf.settings.importer import ImportGlobal
from conf.settings.base import *

im = ImportGlobal()

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']
CURRENT_DOMAIN = 'http://127.0.0.1:8000'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = im.get_env_variable('SECRET_KEY')

#SITE_ID = 1

DATABASES = {'default': {'ENGINE': 'django.db.backends.postgresql_psycopg2',
                         'NAME': im.get_env_variable('DATABASE_NAME'),
                         'USER': im.get_env_variable('DATABASE_USER'),
                         'PASSWORD': im.get_env_variable('DATABASE_PASSWORD'),
                         'HOST': 'localhost',
                         'PORT': ''}}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


# PYTRACKING_CONFIGURATION = {
#     "base_open_tracking_url": CURRENT_DOMAIN + "/open/",
#     "base_click_tracking_url": CURRENT_DOMAIN + "/click/",
# }


# STATICFILES_DIRS += [
#     os.path.join(BASE_DIR, "static"),
# ]