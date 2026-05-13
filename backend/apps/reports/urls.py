from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',   views.dashboard_stats,       name='report-dashboard'),
    path('monthly/',     views.monthly_stats,          name='report-monthly'),
    path('export/excel/',views.export_excel_report,   name='report-export-excel'),
    path('history/',     views.ReportExportListView.as_view(), name='report-history'),
]
