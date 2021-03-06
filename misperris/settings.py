"""
Django settings for misperris project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!ndy9&%xk=(d%w-#zhsu1$*k40hru+t^b(!_@8e#6p#*ue%zp#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#redirigir a la raiz luego de loguearse el usuario
LOGIN_REDIRECT_URL = "/"

LOGOUT_REDIRECT_URL = "/accounts/login"

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'


# Application definition
#facebook
SOCIAL_AUTH_FACEBOOK_KEY = '1785816538212792'
SOCIAL_AUTH_FACEBOOK_SECRET = '99bc641c8c34b7b0f537fcdd7b0d2e33'
#github
SOCIAL_AUTH_GITHUB_KEY = '6a5611a06cac647f97a0'
SOCIAL_AUTH_GITHUB_SECRET = 'a8e3015a037d25af246c7085b6ba4283c8b19093'
#google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '974962742571-1pljd1mprh3m1mu9110tugqnhk90tp6b.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '7D30l09Dm_rbgpUZGQ8ste6F'


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core.apps.CoreConfig',
    'accounts', 
    'social_django',
    'crispy_forms',
    'api',
    'pwa',
]

CRISPY_TEMPLATE_PACK ='bootstrap4'  #libreria booststrap4

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'misperris.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'misperris.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2', # for Facebook authentication
    'social_core.backends.github.GithubOAuth2', # for Github authentication
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.open_id.OpenIdAuth',  # for Google authentication
    'social_core.backends.google.GoogleOpenId',  # for Google authentication
    'social_core.backends.google.GoogleOAuth2',  # for Google authentication

    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_LOGIN_ERROR_URL = '/'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False

PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'serviceworker.js')

PWA_APP_NAME = "Mis Perris"

PWA_APP_ICONS = [
    {
        'src':'/static/core/img/logo_misperris.png',
        'sizes':'160x160'
    }
]