from django.urls import path
from . import views

app_name = 'teams'

urlpatterns = [
    path('', views.teams_home, name='teams'),
    path('<str:teamName>/', views.TeamsDetailView.as_view(), name='teams'),
]
