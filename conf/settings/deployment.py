# -*- coding: utf-8 -*-

""" Local settings.

Django settings for graphite project.
bladibli
Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/

"""

from conf.settings.importer import ImportGlobal
from conf.settings.base import *

im = ImportGlobal()

DEBUG = False
X_FRAME_OPTIONS = 'DENY'
ALLOWED_HOSTS = []
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


#CURRENT_DOMAIN = ''

#ADMINS = ('')

INSTALLED_APPS += (
)

# PYTRACKING_CONFIGURATION = {
#     "base_open_tracking_url": CURRENT_DOMAIN + "/open/",
#     "base_click_tracking_url": CURRENT_DOMAIN + "/click/",
# }

LOCKDOWN_PASSWORDS = ('')
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
LOCKDOWN_URL_EXCEPTIONS = ()

# DATABASES = {'default': {'ENGINE': 'django.db.backends.postgresql_psycopg2',
#                          'NAME': im.get_env_variable('DATABASE_NAME'),
#                          'USER': im.get_env_variable('DATABASE_USER'),
#                          'PASSWORD': im.get_env_variable('DATABASE_PASSWORD'),
#                          'HOST': 'localhost',
#                          'PORT': ''}}

# STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
