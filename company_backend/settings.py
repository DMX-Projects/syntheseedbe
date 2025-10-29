from pathlib import Path
import json
import sys
from django.core.exceptions import ImproperlyConfigured


BASE_DIR = Path(__file__).resolve().parent.parent


SECRETS_FILE = BASE_DIR / 'secrets.json'
try:
    with open(SECRETS_FILE, 'r', encoding='utf-8') as f:
        SECRETS = json.load(f)
except FileNotFoundError:
    SECRETS = {}

def get_secret(key, default=None):
    """Return secret value for `key`. If not found, return `default` (if provided)
    otherwise raise ImproperlyConfigured.
    """
    if key in SECRETS:
        return SECRETS[key]
    if default is not None:
        return default
    raise ImproperlyConfigured(f"Missing required secret: {key}")

# Secret key (prefer secrets.json)
SECRET_KEY = get_secret('SECRET_KEY', 'django-insecure-your-secret-key')
DEBUG = True
ALLOWED_HOSTS = ['https://syntheseed.com', 'www.syntheseed.com', '127.0.0.1', 'localhost']

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'contact',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'company_backend.urls'

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

WSGI_APPLICATION = 'company_backend.wsgi.application'

# Database (PostgreSQL)
# Prefer a `DATABASES` mapping inside secrets.json, otherwise fall back to
# individual keys: DB_ENGINE, DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT.
if 'DATABASES' in SECRETS and isinstance(SECRETS['DATABASES'], dict):
    DATABASES = SECRETS['DATABASES']
else:
    DATABASES = {
        'default': {
            'ENGINE': get_secret('DB_ENGINE', 'django.db.backends.postgresql'),
            'NAME': get_secret('DB_NAME'),
            'USER': get_secret('DB_USER'),
            'PASSWORD': get_secret('DB_PASSWORD'),
            'HOST': get_secret('DB_HOST'),
            'PORT': get_secret('DB_PORT'),
            'OPTION': {
                'sslmode': 'require',
            }
        }
    }

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # React
    "http://localhost:5173",  # Vite
]
# CORS_ALLOW_ALL_ORIGINS = True  # uncomment for testing only

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[{asctime}] {levelname} {name} — {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname}: {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',  # 👈 shows request-related debug info
            'propagate': False,
        },
        'django.security': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'rest_framework': {
            'handlers': ['console'],
            'level': 'DEBUG',  # 👈 shows auth + permission details
            'propagate': False,
        },
    },
}