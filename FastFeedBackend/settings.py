import os
from pathlib import Path

import rest_framework.permissions
from dotenv import load_dotenv

load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=khkw8h@=)9smjtbi)z9i_d&#!22n3xbx22clow+x!81yv2d!x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',

    'corsheaders',

    'admin_interface',
    'colorfield',
    'django.contrib.admin',
    'azbankgateways',

    'rest_framework',
    'rest_framework.authtoken',
    'subs',
    'store',
    'owner',
    'order',
    'menu',
    'comment',
    'payments'
]

X_FRAME_OPTIONS = 'SAMEORIGIN'
SILENCED_SYSTEM_CHECKS = ['security.W019']

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSIONS_CLASSES': (
        'rest_framework.permissions.IsAdminUser', 'rest_framework.permissions.IsAuthenticated'),
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',
                                'rest_framework.filters.SearchFilter',
                                'rest_framework.filters.OrderingFilter',
                                )
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'FastFeedBackend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'FastFeedBackend.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

# use BusinessOwner model instead of the default User model
# AUTH_USER_MODEL = 'core.User'

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

AZ_IRANIAN_BANK_GATEWAYS = {
   'GATEWAYS': {
       'BMI': {
           'MERCHANT_CODE': BMI_MERCHANT_CODE,
           'TERMINAL_CODE': BMI_TERMINAL_CODE,
           'SECRET_KEY': '<YOUR SECRET CODE>',
       },
       'SEP': {
           'MERCHANT_CODE': SEP_MERCHANT_CODE,
           'TERMINAL_CODE': SEP_TERMINAL_CODE,
       },
       'IDPAY': {
           'MERCHANT_CODE': IDPAY_MERCHANT_CODE,
           'METHOD': 'POST',  # GET or POST
           'X_SANDBOX': 1,  # 0 disable, 1 active
       }
   },
   'IS_SAMPLE_FORM_ENABLE': True, # optional, default is inactive
   'DEFAULT': 'IDPAY',
   'CURRENCY': 'IRR', # optional
   'TRACKING_CODE_QUERY_PARAM': 'tc', # optional
   'TRACKING_CODE_LENGTH': 16, # optional
   'SETTING_VALUE_READER_CLASS': 'azbankgateways.readers.DefaultReader', # optional
   'BANK_PRIORITIES': [
       'BMI',
       'SEP',
   ], # optional
}

LANGUAGE_CODE = 'fa'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CORS_ORIGIN_ALLOW_ALL = True
# sms.ir variables
# SMSIR_API_KEY = ''
# SMSIR_PHONE_NUMBER = ''
# SMSIR_API_URL = ''
