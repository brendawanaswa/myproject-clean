"""
Django settings for myproject project (Local Development - Working version)
"""

from pathlib import Path
import os
import dj_database_url  # Make sure this is in requirements.txt

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4a^^l&s^$**82y#9m*v1@219_w^6!pz2d$qkjy48gq45*1-uqv'

# Debug mode for local development
DEBUG = False

ALLOWED_HOSTS = [
    "brendawanaswa.pythonanywhere.com",
    "www.brendawanaswa.pythonanywhere.com",
    "myproject-clean.onrender.com",
    "www.myproject-clean.onrender.com",
    "127.0.0.1",
    "localhost",
]



# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'products',
    'cloudinary',
    'cloudinary_storage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

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

WSGI_APPLICATION = 'myproject.wsgi.application'

# Database
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}"
    )
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'products' / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

import cloudinary
import cloudinary.uploader
import cloudinary.api

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dvl4eohdu',
    'API_KEY': '634961644622524',
    'API_SECRET': 'JcjxO_dQBfSNtN4QbmvABpuATRo',
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Login redirects
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'

# -------------------------------
# Payment keys (Directly added for local dev)
# -------------------------------
PAYSTACK_SECRET_KEY = 'sk_test_89d51599804405cf94f666adeb053ddb3a599bda'
PAYSTACK_PUBLIC_KEY = 'pk_test_3b039c43b8424195377a1b80c44f4ed5ca27c661'
STRIPE_SECRET_KEY = ''  # leave blank if not using Stripe
STRIPE_PUBLISHABLE_KEY = ''
