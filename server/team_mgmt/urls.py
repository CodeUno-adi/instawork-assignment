from django.urls import path
from team_mgmt import views

urlpatterns = [
    path('team-members/', views.TeamList.as_view()),
    path('team-member/<int:pk>/', views.TeamMemberDetail.as_view()),
]