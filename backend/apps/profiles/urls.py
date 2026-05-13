from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('dashboard/',   views.dashboard_kpi,  name='dashboard-kpi'),

    # Quần chúng
    path('my/',          views.MyProfileView.as_view(), name='my-profile'),
    path('my/workflow/', views.ProfileWorkflowView.as_view(), name='my-workflow'),

    # Officer: profile list/detail
    path('',             views.ProfileListView.as_view(),          name='profile-list'),
    path('<int:pk>/',    views.ProfileDetailView.as_view(),         name='profile-detail'),
    path('<int:pk>/workflow/', views.ProfileWorkflowView.as_view(), name='profile-workflow'),
    path('<int:pk>/assign-officer/', views.AssignOfficerView.as_view(), name='assign-officer'),
    path('<int:pk>/ai-scan/', views.ai_scan_results, name='ai-scan'),

    # Reviews & comments
    path('<int:profile_id>/reviews/', views.ProfileReviewListView.as_view(), name='profile-reviews'),
    path('<int:profile_id>/committee-comment/', views.CommitteeCommentView.as_view(), name='committee-comment'),
]
