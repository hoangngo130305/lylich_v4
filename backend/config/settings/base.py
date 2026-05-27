"""
Base settings shared by all environments.
"""
import os
from pathlib import Path
from datetime import timedelta
from decouple import config, Csv

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = config('SECRET_KEY', default='django-insecure-change-in-production')

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1', cast=Csv())

# ── Installed Apps ───────────────────────────────────────────────────────────
DJANGO_APPS = [
    'unfold',
    'unfold.contrib.filters',
    'unfold.contrib.forms',
    'unfold.contrib.import_export',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'corsheaders',
    'django_filters',
    'drf_yasg',
    'drf_spectacular',
    'import_export',
    'django_celery_beat',
    'django_celery_results',
]

LOCAL_APPS = [
    'apps.common',
    'apps.accounts',
    'apps.uploads',
    'apps.profiles',
    'apps.family',
    'apps.timelines',
    'apps.verification',
    'apps.notifications',
    'apps.exports',
    'apps.reports',
    'apps.auditlogs',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# ── Middleware ───────────────────────────────────────────────────────────────
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'apps.auditlogs.middleware.RequestLogMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'
ASGI_APPLICATION = 'config.asgi.application'

# ── Database ─────────────────────────────────────────────────────────────────
DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE', default='django.db.backends.mysql'),
        'NAME': config('DB_NAME', default='lylich_dang'),
        'USER': config('DB_USER', default='root'),
        'PASSWORD': config('DB_PASSWORD', default=''),
        'HOST': config('DB_HOST', default='127.0.0.1'),
        'PORT': config('DB_PORT', default='3306'),
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES', time_zone='+07:00'",
            'connect_timeout': 10,
        },
        'TEST': {
            'NAME': 'test_lylich_dang',
            'CHARSET': 'utf8mb4',
            'COLLATION': 'utf8mb4_unicode_ci',
        },
    }
}

# ── Custom User Model ─────────────────────────────────────────────────────────
AUTH_USER_MODEL = 'accounts.User'

# ── Password Validation ───────────────────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', 'OPTIONS': {'min_length': 8}},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ── Internationalization ──────────────────────────────────────────────────────
LANGUAGE_CODE = 'vi'
TIME_ZONE = 'Asia/Ho_Chi_Minh'
USE_I18N = True
USE_TZ = False

# ── Static & Media Files ──────────────────────────────────────────────────────
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = config('MEDIA_ROOT', default=str(BASE_DIR / 'media'))

MAX_UPLOAD_SIZE = config('MAX_UPLOAD_SIZE_MB', default=10, cast=int) * 1024 * 1024

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ── Django REST Framework ─────────────────────────────────────────────────────
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FormParser',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ),
    'DEFAULT_PAGINATION_CLASS': 'apps.common.pagination.StandardResultsSetPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'EXCEPTION_HANDLER': 'apps.common.exceptions.custom_exception_handler',
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '20/minute',
        'user': '200/minute',
        'login': '5/minute',
    },
}

# ── JWT Settings ──────────────────────────────────────────────────────────────
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=config('JWT_ACCESS_TOKEN_LIFETIME_MINUTES', default=60, cast=int)),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=config('JWT_REFRESH_TOKEN_LIFETIME_DAYS', default=7, cast=int)),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': config('JWT_SIGNING_KEY', default=SECRET_KEY),
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'JTI_CLAIM': 'jti',
    'TOKEN_OBTAIN_SERIALIZER': 'apps.accounts.serializers.CustomTokenObtainPairSerializer',
}

# ── CORS ──────────────────────────────────────────────────────────────────────
CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS', default='http://localhost:8080,http://localhost:3000', cast=Csv())
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = [
    'accept', 'accept-encoding', 'authorization', 'content-type',
    'dnt', 'origin', 'user-agent', 'x-csrftoken', 'x-requested-with',
]

# ── Celery ────────────────────────────────────────────────────────────────────
CELERY_BROKER_URL = config('CELERY_BROKER_URL', default='redis://127.0.0.1:6379/1')
CELERY_RESULT_BACKEND = config('CELERY_RESULT_BACKEND', default='redis://127.0.0.1:6379/2')
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 300

# ── Cache ─────────────────────────────────────────────────────────────────────
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': config('REDIS_URL', default='redis://127.0.0.1:6379/0'),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
        'KEY_PREFIX': 'lylich',
        'TIMEOUT': 300,
    }
}

# ── Email ─────────────────────────────────────────────────────────────────────
EMAIL_BACKEND = config('EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')
EMAIL_HOST = config('EMAIL_HOST', default='localhost')
EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=False, cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='noreply@lylich.gov.vn')

# ── drf-spectacular (OpenAPI) ─────────────────────────────────────────────────
SPECTACULAR_SETTINGS = {
    'TITLE': 'Hệ Thống Kê Khai Lý Lịch Đảng API',
    'DESCRIPTION': 'API backend cho hệ thống kê khai Lý lịch Đảng viên — Mẫu 2-KNĐ',
    'VERSION': '3.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'COMPONENT_SPLIT_REQUEST': True,
    'SORT_OPERATIONS': False,
}

# ── drf-yasg (Swagger) ────────────────────────────────────────────────────────
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
        }
    },
    'USE_SESSION_AUTH': False,
    'JSON_EDITOR': True,
    'PERSIST_AUTH': True,
}

# ── Unfold Admin ──────────────────────────────────────────────────────────────
UNFOLD = {
    'SITE_TITLE': 'Ban Xây Dựng Đảng',
    'SITE_HEADER': 'Hệ Thống Lý Lịch Đảng',
    'SITE_URL': '/',
    'SITE_ICON': None,
    'SITE_FAVICON': None,
    'COLORS': {
        'primary': {
            '50': '254 242 242',
            '100': '254 226 226',
            '200': '252 205 205',
            '300': '250 170 170',
            '400': '247 128 128',
            '500': '239 68 68',
            '600': '220 38 38',
            '700': '185 28 28',
            '800': '153 27 27',
            '900': '127 29 29',
            '950': '69 10 10',
        },
    },
    'SIDEBAR': {
        'show_search': True,
        'show_all_applications': True,
        'navigation': [
            {
                'title': 'Tổng quan',
                'separator': True,
                'items': [
                    {'title': 'Dashboard', 'icon': 'dashboard', 'link': '/admin/'},
                ],
            },
            {
                'title': 'Quản lý người dùng',
                'separator': True,
                'items': [
                    {'title': 'Người dùng', 'icon': 'people', 'link': '/admin/accounts/user/'},
                    {'title': 'Vai trò', 'icon': 'admin_panel_settings', 'link': '/admin/accounts/role/'},
                    {'title': 'Cán bộ Đảng', 'icon': 'manage_accounts', 'link': '/admin/accounts/officer/'},
                    {'title': 'Lịch sử đăng nhập', 'icon': 'history', 'link': '/admin/accounts/loginhistory/'},
                ],
            },
            {
                'title': 'Hồ sơ lý lịch',
                'separator': True,
                'items': [
                    {'title': 'Hồ sơ', 'icon': 'folder_shared', 'link': '/admin/profiles/profile/'},
                    {'title': 'Thành viên gia đình', 'icon': 'family_restroom', 'link': '/admin/family/familymember/'},
                    {'title': 'Lịch sử thẩm định', 'icon': 'rate_review', 'link': '/admin/profiles/profilereview/'},
                    {'title': 'Yêu cầu bổ sung', 'icon': 'edit_note', 'link': '/admin/exports/profilecorrectionrequest/'},
                ],
            },
            {
                'title': 'Xác minh',
                'separator': True,
                'items': [
                    {'title': 'Yêu cầu xác minh', 'icon': 'verified_user', 'link': '/admin/verification/verificationrequest/'},
                ],
            },
            {
                'title': 'Thông báo',
                'separator': True,
                'items': [
                    {'title': 'Thông báo', 'icon': 'notifications', 'link': '/admin/notifications/notification/'},
                    {'title': 'Mẫu thông báo', 'icon': 'message', 'link': '/admin/notifications/notificationtemplate/'},
                ],
            },
            {
                'title': 'Báo cáo & Xuất',
                'separator': True,
                'items': [
                    {'title': 'Xuất Word', 'icon': 'description', 'link': '/admin/exports/wordexportlog/'},
                    {'title': 'Xuất báo cáo', 'icon': 'analytics', 'link': '/admin/reports/reportexport/'},
                ],
            },
            {
                'title': 'Danh mục',
                'separator': True,
                'items': [
                    {'title': 'Dân tộc', 'icon': 'public', 'link': '/admin/common/ethnicgroup/'},
                    {'title': 'Tôn giáo', 'icon': 'church', 'link': '/admin/common/religion/'},
                    {'title': 'Đơn vị hành chính', 'icon': 'location_city', 'link': '/admin/common/administrativeunit/'},
                ],
            },
        ],
    },
}

# ── Frontend ──────────────────────────────────────────────────────────────────
FRONTEND_URL = config('FRONTEND_URL', default='http://localhost:8080')

# ── External Services ─────────────────────────────────────────────────────────
ZALO_OA_TOKEN = config('ZALO_OA_TOKEN', default='')
ZALO_OA_ID = config('ZALO_OA_ID', default='')
SMS_API_KEY = config('SMS_API_KEY', default='')
SMS_API_URL = config('SMS_API_URL', default='')

# ── Logging ───────────────────────────────────────────────────────────────────
LOG_LEVEL = config('LOG_LEVEL', default='INFO')
LOG_FILE = config('LOG_FILE', default=str(BASE_DIR / 'logs' / 'django.log'))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {asctime} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_FILE,
            'maxBytes': 10 * 1024 * 1024,
            'backupCount': 5,
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': LOG_LEVEL,
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'WARNING',
            'propagate': False,
        },
        'apps': {
            'handlers': ['console', 'file'],
            'level': LOG_LEVEL,
            'propagate': False,
        },
    },
}
