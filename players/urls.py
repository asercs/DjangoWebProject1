from django.urls import path
from . import views

app_name = 'players'


urlpatterns = [
    path('', views.players_home, name='players'),
    path('<str:nickname>/', views.PlayersDetailView.as_view(), name='players'),
]
