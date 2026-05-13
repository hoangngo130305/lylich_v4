from django.urls import path
from . import views

urlpatterns = [
    path('edit-history/',                       views.EditHistoryListView.as_view(),            name='edit-history-list'),
    path('edit-history/<int:profile_id>/',      views.EditHistoryListView.as_view(),            name='edit-history-profile'),
    path('corrections/',                        views.CorrectionRequestListCreateView.as_view(),name='correction-list'),
    path('corrections/<int:pk>/',               views.CorrectionRequestDetailView.as_view(),    name='correction-detail'),
    path('corrections/items/<int:pk>/',         views.update_correction_item,                   name='correction-item-update'),
    path('word/<int:profile_id>/',              views.export_word,                              name='export-word'),
    path('word-logs/',                          views.WordExportLogListView.as_view(),          name='word-log-list'),
]
