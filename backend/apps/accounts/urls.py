from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('login/',          views.LoginView.as_view(),               name='login'),
    path('logout/',         views.LogoutView.as_view(),              name='logout'),
    path('token/refresh/',  views.TokenRefreshViewCustom.as_view(),  name='token-refresh'),
    path('register/',       views.RegisterView.as_view(),            name='register'),
    path('me/',             views.MeView.as_view(),                  name='me'),
    path('admin-session/',  views.AdminSessionLoginView.as_view(),   name='admin-session'),

    # Password
    path('password/change/',          views.ChangePasswordView.as_view(),       name='password-change'),
    path('password/reset/',           views.PasswordResetRequestView.as_view(), name='password-reset-request'),
    path('password/reset/confirm/',   views.PasswordResetConfirmView.as_view(), name='password-reset-confirm'),

    # User management (officers)
    path('users/',            views.UserListView.as_view(),       name='user-list'),
    path('users/<int:pk>/',   views.UserDetailView.as_view(),     name='user-detail'),
    path('users/<int:pk>/toggle-status/', views.toggle_user_status, name='user-toggle-status'),
    path('users/<int:pk>/hard-delete/', views.UserHardDeleteView.as_view(), name='user-hard-delete'),
    path('users/<int:user_id>/login-history/', views.LoginHistoryListView.as_view(), name='user-login-history'),

    # Account requests
    path('account-requests/',          views.AccountRequestListView.as_view(),   name='account-request-list'),
    path('account-requests/<int:pk>/', views.AccountRequestDetailView.as_view(), name='account-request-detail'),

    # ── Super Admin ──────────────────────────────────────────────────────────
    path('superadmin/login/',                          views.SuperAdminLoginView.as_view(),       name='superadmin-login'),
    path('superadmin/officers/',                       views.OfficerListCreateView.as_view(),     name='superadmin-officer-list'),
    path('superadmin/officers/<int:pk>/',              views.OfficerDetailView.as_view(),         name='superadmin-officer-detail'),
    path('superadmin/officers/<int:pk>/permissions/', views.OfficerPermissionView.as_view(),     name='superadmin-officer-permissions'),
    path('superadmin/officers/<int:pk>/reset-password/', views.officer_reset_password,           name='superadmin-officer-reset-password'),
]
