from django.urls import path
from . import views

urlpatterns = [
    path('ethnic-groups/', views.EthnicGroupListView.as_view(), name='ethnic-group-list'),
    path('religions/', views.ReligionListView.as_view(), name='religion-list'),
    path('education-levels/', views.EducationLevelListView.as_view(), name='education-level-list'),
    path('political-levels/', views.PoliticalLevelListView.as_view(), name='political-level-list'),
    path('administrative-units/', views.AdministrativeUnitListView.as_view(), name='admin-unit-list'),
]
