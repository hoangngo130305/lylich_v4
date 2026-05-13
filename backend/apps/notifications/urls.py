from django.urls import path
from . import views

urlpatterns = [
    path('',                      views.NotificationListView.as_view(), name='notification-list'),
    path('stats/',                views.notification_stats,             name='notification-stats'),
    path('<int:pk>/read/',        views.mark_read,                      name='notification-read'),
    path('read-all/',             views.mark_all_read,                  name='notification-read-all'),
    path('send/',                 views.send_notification,              name='notification-send'),
    path('bulk-send/',            views.bulk_send,                      name='notification-bulk-send'),
    path('templates/',            views.NotificationTemplateListView.as_view(),  name='template-list'),
    path('templates/<int:pk>/',   views.NotificationTemplateDetailView.as_view(),name='template-detail'),
]
