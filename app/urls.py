from unicodedata import name
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
   
    path('', views.index, name='index'),
    path('login', views.user_login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('tabular', views.tabular, name='tabular'),
    
    path('<filename>.html', views.html),
    path('check_username', views.check_username, name='check-username'),

    ]
