from django.urls import path
from . import views

urlpatterns = [
    path('',          views.VerificationListCreateView.as_view(), name='verification-list'),
    path('stats/',    views.verification_stats,                   name='verification-stats'),
    path('<int:pk>/', views.VerificationDetailView.as_view(),     name='verification-detail'),
    path('<int:pk>/remind/',   views.send_reminder,               name='verification-remind'),
    path('<int:pk>/received/', views.mark_received,               name='verification-received'),
]
