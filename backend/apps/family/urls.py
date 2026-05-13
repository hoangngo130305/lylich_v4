from django.urls import path
from . import views

urlpatterns = [
    path('<int:profile_id>/members/',          views.FamilyMemberListCreateView.as_view(), name='family-list'),
    path('<int:profile_id>/members/<int:pk>/', views.FamilyMemberDetailView.as_view(),     name='family-detail'),
]
