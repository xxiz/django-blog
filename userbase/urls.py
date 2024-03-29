from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='userbase-register'),
    path('login/', auth_views.LoginView.as_view(template_name='userbase/login.htm'), name='userbase-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='userbase/logout.htm'), name='userbase-logout'),
    path('profile/', views.profile, name='userbase-profile'),
]
