"""
Django settings for admin_proj project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i+homa9tttt*pwd&=zs3&ttmmviqmas^p2pei^3v4v3u2j==_d62+7ov'
 
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =   True

 
TEMPLATED_DOCS_LIBREOFFICE_PATH =  'C://Program Files/LibreOffice/program'
PROJECT_ROOT   =   os.path.join(os.path.abspath(__file__))
ALLOWED_HOSTS = ['167.99.51.57','127.0.0.1']
 
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'admin_app',
    'Finance',
    'crispy_forms',
    'django_filters',
    'widget_tweaks',
    'bootstrap_datepicker_plus',
    'bookapp',
  
    
    'django_select2',
    # 'dal_legacy_static',
    # 'grappelli',
    'django_po',
    #'templated_docs',
    'SecurityGuard',
   # 'herokuapp',
   
    
]
CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
     
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'erp_proj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'erp_proj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
# if DEBUG:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql',
            
#             'NAME':'uerpdb1',
#             'USER':'postgres',
#             'PASSWORD':'123456',
#             'PORT':'5432',
#             'ATOMIC_REQUESTS': True,
#         }
#     }
    
# else:
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'uerpdb1',
            'USER': 'issa',
            'PASSWORD': '123456',
            'HOST': 'localhost',
            'PORT': '',
            'ATOMIC_REQUESTS': True,
        }
    }

   
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/
 
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

# STATIC_URL = '/static/'
# MEDIA_URL = '/images/'
 
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static')
# ]
# # STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# MEDIA_ROOT=os.path.join(BASE_DIR,'static/images')
 

STATIC_URL = '/static/'
MEDIA_URL = '/images/'
 
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT=os.path.join(BASE_DIR,'static/images')