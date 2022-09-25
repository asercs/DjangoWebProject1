from django.urls import path
from . import views

app_name = 'matches'

urlpatterns = [
    path('', views.matches_home, name='matches'),
    path('<int:pk>', views.MatchesDetailView.as_view(), name='matches'),
]
