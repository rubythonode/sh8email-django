"""
Django settings for sh8email project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
import os

from .settings_common import ALLOWED_HOSTS as COMMON_ALLOWED_HOSTS
from .settings_common import BASE_DIR as COMMON_BASE_DIR
from .settings_common import INSTALLED_APPS as COMMON_INSTALLED_APPS
from .settings_common import LANGUAGE_CODE as COMMON_LANGUAGE_CODE
from .settings_common import MAIL_SERVER_PORT as COMMON_MAIL_SERVER_PORT
from .settings_common import MIDDLEWARE_CLASSES as COMMON_MIDDLEWARE_CLASSES
from .settings_common import ROOT_URLCONF as COMMON_ROOT_URLCONF
from .settings_common import SANITIZER_ALLOWED_ATTRIBUTES as COMMON_SANITIZER_ALLOWED_ATTRIBUTES
from .settings_common import SANITIZER_ALLOWED_STYLES as COMMON_SANITIZER_ALLOWED_STYLES
from .settings_common import SANITIZER_ALLOWED_TAGS as COMMON_SANITIZER_ALLOWED_TAGS
from .settings_common import STATIC_ROOT as COMMON_STATIC_ROOT
from .settings_common import STATIC_URL as COMMON_STATIC_URL
from .settings_common import TEMPLATES as COMMON_TEMPLATES
from .settings_common import TIME_ZONE as COMMON_TIME_ZONE
from .settings_common import USE_I18N as COMMON_USE_I18N
from .settings_common import USE_L10N as COMMON_USE_L10N
from .settings_common import USE_TZ as COMMON_USE_TZ
from .settings_common import WSGI_APPLICATION as COMMON_WSGI_APPLICATION

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = COMMON_BASE_DIR

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q&xot8*fg$b4dd9c1$+fqqj4!t4e%jk_3=un#!g9*!q%(_t@zd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = COMMON_INSTALLED_APPS

MIDDLEWARE_CLASSES = COMMON_MIDDLEWARE_CLASSES

ROOT_URLCONF = COMMON_ROOT_URLCONF

TEMPLATES = COMMON_TEMPLATES

WSGI_APPLICATION = COMMON_WSGI_APPLICATION


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sh8email',
        'USER': 'sh8email',
        'PASSWORD': os.getenv('SH8EMAIL_DB_PASSWORD', 'password'),
        'HOST': 'localhost',
        'POST': '5432'
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = COMMON_LANGUAGE_CODE

TIME_ZONE = COMMON_TIME_ZONE

USE_I18N = COMMON_USE_I18N

USE_L10N = COMMON_USE_L10N

USE_TZ = COMMON_USE_TZ


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/ls

STATIC_URL = COMMON_STATIC_URL
STATIC_ROOT = COMMON_STATIC_ROOT

# Mail receiving server settings
MAIL_SERVER_PORT = COMMON_MAIL_SERVER_PORT

# html_sanitizer settings
SANITIZER_ALLOWED_TAGS = COMMON_SANITIZER_ALLOWED_TAGS
SANITIZER_ALLOWED_ATTRIBUTES = COMMON_SANITIZER_ALLOWED_ATTRIBUTES
SANITIZER_ALLOWED_STYLES = COMMON_SANITIZER_ALLOWED_STYLES


