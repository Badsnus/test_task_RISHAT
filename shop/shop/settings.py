import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'NO_SECRET_KEY')

DEBUG = os.getenv('DEBUG', default='OFF').lower() in ('on', 'yes', 'true')

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')

SITE_DOMAIN = os.getenv('SITE_DOMAIN', 'http://127.0.0.1:8000')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'products.apps.ProductsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'shop.wsgi.application'

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

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# STRIPE
STRIPE_PUBLIC_KEY = os.getenv(
    'STRIPE_PUBLIC_KEY',
    'pk_test_51MdtN6CFtYKwUqnVZzeri4mgM2VdjcrcvxbDidzosOOdyIof6y7YmngZCK9CgacsYImUGdwOoHB359TBdZ4MQxUJ00CAoI7Cxj',
)
STRIPE_SECRET_KEY = os.getenv(
    'STRIPE_SECRET_KEY',
    'sk_test_51MdtN6CFtYKwUqnVAqVd4ZLV8GAapZzOgZi3CqD7aMvZ7NuVdC0fCT1u4EDVzjq8aT0SBJxHJskdoHEQHg9kkvu100pPUJ1JEE',
)
