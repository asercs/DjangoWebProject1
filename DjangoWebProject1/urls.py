"""
Definition of urls for DjangoWebProject1.
"""
from django.conf import settings
from django.conf.urls.static import static
from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
import grappelli
from django.conf.urls import include

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('privacy/', views.privacy, name='privacy'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls, name='admin'), # admin site
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('teams/', include('teams.urls', namespace='teams'), name='teams'),
    path('players/', include('players.urls', namespace='players'), name='players'),
    path('matches/', include('matches.urls', namespace='matches'), name='matches'),
    path('market/', include('market.urls', namespace='market'), name='market'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'app.views.handler404'
handler500 = 'app.views.handler500'