from django.urls import path
from . import views

urlpatterns = [
    path('activity/',            views.ActivityLogListView.as_view(),    name='activity-log-list'),
    path('ai-scan/',             views.AIScanResultListView.as_view(),   name='ai-scan-list'),
    path('ai-scan/<int:pk>/',    views.AIScanResultDetailView.as_view(), name='ai-scan-detail'),
]
