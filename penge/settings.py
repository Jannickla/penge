import os
import warnings
from django.utils.translation import ugettext_lazy as _
from os.path import dirname

warnings.simplefilter('error', DeprecationWarning)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CONTENT_DIR = os.path.join(BASE_DIR, 'content')

SECRET_KEY = '6l$lvt^-q1n_ziwje!m06slj41qu6=wve6ca-k7u&0=pkm$d(n'

DEBUG = True
ALLOWED_HOSTS = []

SITE_ID = 1

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'rest_framework',
    'rest_framework.authtoken',

    # Third party apps
    'bootstrap4',  # Get replacement for this app
    'django_countries',
    'formtools',  # Get replacement for this app
    'tinymce',
    'djstripe',  # Get replacement for this app
    'svg',  # Get replacement for this app
    'notifications',

    # Application apps
    'accounts',
    'dashboard',
    'feedback',
    'goals',
    'website',
    'blog',
    'marketing',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'penge.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(CONTENT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'penge.context_processors.feedback_form',  # Custom
                'penge.context_processors.email_subscription_form',  # Custom
            ],
        },
    },
]

# WSGI
WSGI_APPLICATION = 'penge.wsgi.application'

# Email Settings
# EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_FILE_PATH = os.path.join(CONTENT_DIR, 'tmp/../content/templates/emails')
EMAIL_HOST_USER = 'test@example.com'
DEFAULT_FROM_EMAIL = 'test@example.com'

# Databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Authentication
LOGIN_REDIRECT_URL = 'index'
LOGIN_URL = 'accounts:login'
AUTH_USER_MODEL = 'accounts.Account'
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

# Message Storage
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

# Multiple Languages
USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('en', _('English')),
    ('pl', _('Polish')),
    ('da', _('Danish')),
    ('se', _('Swedish')),
    ('no', _('Norwegian')),
]
LOCALE_PATHS = [
    os.path.join(CONTENT_DIR, 'locale'),
]

# Time Zone
TIME_ZONE = 'UTC'
USE_TZ = True

# Media Files
MEDIA_ROOT = os.path.join(CONTENT_DIR, 'media')
MEDIA_URL = '/media/'

# Static Files
STATIC_ROOT = os.path.join(CONTENT_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(CONTENT_DIR, 'assets'),
]

# TinyMCE Settings
TINYMCE_DEFAULT_CONFIG = {
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
}

# MailChimp Settings
MAILCHIMP_API_KEY = ''
MAILCHIMP_DATA_CENTER = ''
MAILCHIMP_EMAIL_LIST_ID = ''

# REST Session Authentication
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    )
}

# Stripe Settings
STRIPE_TEST_PUBLIC_KEY = os.environ.get("STRIPE_TEST_PUBLIC_KEY", "pk_test_51HNe8AGKAfw8uKC59Jf7GhygdwVxa6IjRSofBHomCRUfuZdvVOLJsdGgfBnJcsDFVKZ2JLFvLdqmE5go5vxS37CF00Siec7L0k")
STRIPE_TEST_SECRET_KEY = os.environ.get("STRIPE_TEST_SECRET_KEY", "sk_test_51HNe8AGKAfw8uKC5Y24cmGEnN7TWvACkhF8350n6ok035ZCubC9Ns2cdxJqUUBxNNgudAOzRq8ghRLHhFI3ybVYv00XwSz9S6z")
STRIPE_LIVE_MODE = False
DJSTRIPE_WEBHOOK_SECRET = "whsec_xxx"  # We don't use this, but it must be set

# SVG Template Tag
SVG_DIRS = [
    os.path.join(CONTENT_DIR, 'svg-img')
]
