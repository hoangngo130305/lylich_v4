from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

# Dev DB — SQLite for quick start, or MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME', default='lylich_dang'),
        'USER': config('DB_USER', default='root'),
        'PASSWORD': config('DB_PASSWORD', default=''),
        'HOST': config('DB_HOST', default='127.0.0.1'),
        'PORT': config('DB_PORT', default='3306'),
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES', time_zone='+07:00'",
        },
    }
}

# Allow all CORS in dev
CORS_ALLOW_ALL_ORIGINS = True

# Show SQL queries in dev
LOGGING['loggers']['django.db.backends'] = {
    'level': 'DEBUG',
    'handlers': ['console'],
    'propagate': False,
}

# Dev email (console)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Disable throttling in dev
REST_FRAMEWORK['DEFAULT_THROTTLE_CLASSES'] = []

# Show full Swagger UI
REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
    'rest_framework.renderers.JSONRenderer',
    'rest_framework.renderers.BrowsableAPIRenderer',
)

# Simpler cache in dev
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
