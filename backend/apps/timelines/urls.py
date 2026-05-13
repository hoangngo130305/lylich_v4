from django.urls import path
from . import views

urlpatterns = [
    path('<int:profile_id>/all/',             views.all_sections,                    name='all-sections'),
    path('<int:profile_id>/history/',         views.HistoryListCreate.as_view(),     name='history-list'),
    path('<int:profile_id>/history/<int:pk>/',views.HistoryDetail.as_view(),         name='history-detail'),
    path('<int:profile_id>/work/',            views.WorkListCreate.as_view(),        name='work-list'),
    path('<int:profile_id>/work/<int:pk>/',   views.WorkDetail.as_view(),            name='work-detail'),
    path('<int:profile_id>/education/',       views.EducationListCreate.as_view(),   name='education-list'),
    path('<int:profile_id>/education/<int:pk>/', views.EducationDetail.as_view(),   name='education-detail'),
    path('<int:profile_id>/org/',             views.OrgListCreate.as_view(),         name='org-list'),
    path('<int:profile_id>/org/<int:pk>/',    views.OrgDetail.as_view(),             name='org-detail'),
    path('<int:profile_id>/awards/',          views.AwardListCreate.as_view(),       name='award-list'),
    path('<int:profile_id>/awards/<int:pk>/', views.AwardDetail.as_view(),           name='award-detail'),
    path('<int:profile_id>/travel/',          views.TravelListCreate.as_view(),      name='travel-list'),
    path('<int:profile_id>/travel/<int:pk>/', views.TravelDetail.as_view(),          name='travel-detail'),
    path('<int:profile_id>/relatives/',       views.RelativeListCreate.as_view(),    name='relative-list'),
    path('<int:profile_id>/relatives/<int:pk>/', views.RelativeDetail.as_view(),    name='relative-detail'),
]
