import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.getenv('DJANGO_KEY',
                       default='django-insecure-3bo0xtjgg3(_a%o1b#%1os_(#5yu$4tr^=xb&%^8x@f__0np@5')

DEBUG = False

ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1']


INSTALLED_APPS = [
    'core.apps.CoreConfig',
    'rating.apps.RatingConfig',
    'users.apps.UsersConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'invite_users.urls'

TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'invite_users.wsgi.application'


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', default='django.db.backends.postgresql'),
        'NAME': os.getenv('DB_NAME', default='postgres'),
        'USER': os.getenv('POSTGRES_USER', default='postgres'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', default='postgres'),
        'HOST': os.getenv('DB_HOST', default='db'),
        'PORT': os.getenv('DB_PORT', default='5432')
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


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST',
                            default='django.app@yandex.ru')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD',
                                default='][p123!@#')
EMAIL_PORT = os.getenv('EMAIL_PORT',
                       default=587)

LOGIN_URL = 'users:login'
LOGIN_REDIRECT_URL = 'rating:scores'

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = 'code/static/'
# STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static/'),)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'users.User'
