from django.urls import path
from . import views

app_name = 'market'

urlpatterns = [
    path('', views.market_home, name='market'),
    path('<int:pk>', views.MarketDetailView.as_view(), name='market'),
]

