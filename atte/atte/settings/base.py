# Django settings for atte project.

import os
import re
from os.path import join, abspath, dirname


here = lambda *x: join(abspath(dirname(__file__)), *x)
PROJECT_ROOT = here("..", "..")
root = lambda *x: join(abspath(PROJECT_ROOT), *x)
SERVICE_HOST = "http://localhost:8000"
DEBUG = True
TEMPLATE_DEBUG = DEBUG

def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s env variable" % var_name
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_env_variable('DJANGO_SECRET_KEY')
        
ADMINS = (
    ('TaeYun Lee', 'ok7217@gmail.com'),
    ('Mingi Kim', 'mgsmurf@mgail.com')
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': root('atte.sqlite3'),                      # Or path to database file if using sqlite3.
    }
}

ALLOWED_HOSTS = ['.atte.kr']
TIME_ZONE = 'Asia/Seoul'
LANGUAGE_CODE = 'ko-kr'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = root('media')
MEDIA_URL = '/media/'
DATETIME_FORMAT=('Y-m-d H:i:s')
DATE_FORMAT=('Y-m-d')
# STATIC_ROOT = ''

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    root('static')
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'atte.urls'

WSGI_APPLICATION = 'atte.wsgi.application'

TEMPLATE_DIRS = (
    root('templates'),
)

DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs'
]

ATTE_APPS = [
    'playlists',
    'accounts'
]

THIRD_PARTY_APPS = [
    'django_extensions',
    'tastypie',
]

INSTALLED_APPS = DJANGO_APPS + ATTE_APPS + THIRD_PARTY_APPS

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
