import os
import sys
import dj_database_url
from decimal import Decimal
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Security
SECRET_KEY = os.getenv("SECRET_KEY", "your-default-secret-key")  # Set in Railway Variables
DEBUG = os.getenv("DEBUG", "False") == "True"
# Allowed Hosts (Railway URL + localhost)
ALLOWED_HOSTS = ["localhost", "127.0.0.1", os.getenv("RAILWAY_URL", ".railway.app")]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    'accounts',
    'sorl.thumbnail',
    'widget_tweaks',
    'products',
    'cart',
    'orders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # for static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'toystore.urls'

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

WSGI_APPLICATION = 'toystore.wsgi.application'

# Database (Railway provides DATABASE_URL automatically)
DATABASES = {
    "default": dj_database_url.config(
        default="sqlite:///db.sqlite3", conn_max_age=600, ssl_require=False
    )
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': BASE_DIR / 'cache',
    }
}


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]  # your custom static files
STATIC_ROOT = BASE_DIR / "staticfiles"    # where collectstatic will put all files

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


#cart tax added
INDIAN_TAX_RATES = {
    'GST': {
        'cgst': Decimal('0.09'),  # 9% Central GST
        'sgst': Decimal('0.09'),  # 9% State GST
        'igst': Decimal('0.18'),  # 18% Integrated GST (for inter-state)
    },
    # You can add more tax slabs (5%, 12%, 28% etc.)
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
