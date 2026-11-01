"""
INF601 - Advanced Programming in Python
Ray Bednara
Mini Project 6
"""
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/add/', views.add_course, name='add_course'),
    path('rounds/new/', views.new_round, name='new_round'),
    path('rounds/<int:pk>/', views.round_detail, name='round_detail'),
    path('rounds/<int:pk>/score/', views.add_score, name='add_score'),
    path('register/', views.register, name='register'),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='registration/login.html', authentication_form=LoginForm),
        name='login',
    ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
