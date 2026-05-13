from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

# ── Swagger / OpenAPI ────────────────────────────────────────────────────────
schema_view = get_schema_view(
    openapi.Info(
        title='Hệ Thống Kê Khai Lý Lịch Đảng API',
        default_version='v3',
        description='API backend Mẫu 2-KNĐ — Ban Xây Dựng Đảng',
        contact=openapi.Contact(email='admin@lylich.gov.vn'),
        license=openapi.License(name='Internal Use Only'),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

API_PREFIX = 'api/v1'

urlpatterns = [
    # ── Admin ──────────────────────────────────────────────────────────────
    path('admin/', admin.site.urls),

    # ── API Routes ─────────────────────────────────────────────────────────
    path(f'{API_PREFIX}/auth/', include('apps.accounts.urls')),
    path(f'{API_PREFIX}/common/', include('apps.common.urls')),
    path(f'{API_PREFIX}/uploads/', include('apps.uploads.urls')),
    path(f'{API_PREFIX}/profiles/', include('apps.profiles.urls')),
    path(f'{API_PREFIX}/family/', include('apps.family.urls')),
    path(f'{API_PREFIX}/timelines/', include('apps.timelines.urls')),
    path(f'{API_PREFIX}/verification/', include('apps.verification.urls')),
    path(f'{API_PREFIX}/notifications/', include('apps.notifications.urls')),
    path(f'{API_PREFIX}/exports/', include('apps.exports.urls')),
    path(f'{API_PREFIX}/reports/', include('apps.reports.urls')),
    path(f'{API_PREFIX}/auditlogs/', include('apps.auditlogs.urls')),

    # ── API Docs (Swagger) ─────────────────────────────────────────────────
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # ── drf-spectacular ────────────────────────────────────────────────────
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
