import os
from pathlib import Path
from .config import config
import celery

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-8go1*j$sz7x3tqaq9xb!hj#rz)v06_jmhwrwklb_$$5-8y^#ks'


DEBUG = True

ALLOWED_HOSTS = ['158.160.129.2', '127.0.0.1']

DEFAULT_IMG_URL = ('https://cdn.dribbble.com/users/55871/screenshots/2158022/media/'
                   '8f2a4a2c9126a9f265fb9e1023b1698a.jpg?resize=400x0')

CELERY_BROKER_URL = 'redis://redis:6379/0'


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',

    'event_app',
    'file_uploader_app',
    'mailing_app',
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'yandex_case.urls'

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

WSGI_APPLICATION = 'yandex_case.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOW_ALL_ORIGINS = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    # 'DEFAULT_RENDERER_CLASSES': (
    #     'rest_framework.renderers.JSONRenderer',
    # )
}

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')
MEDIA_URL = '/media/'


mail_cfg = config.get('mail')

EMAIL_HOST = mail_cfg.get('EMAIL_HOST')
EMAIL_PORT = mail_cfg.get('EMAIL_PORT')
EMAIL_USE_TLS = mail_cfg.get('EMAIL_USE_TLS')
EMAIL_USE_SSL = mail_cfg.get('EMAIL_USE_SSL')
EMAIL_HOST_USER = mail_cfg.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = mail_cfg.get('EMAIL_HOST_PASSWORD')
