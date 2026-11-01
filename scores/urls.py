"""
INF601 - Advanced Programming in Python
Ray Bednara
Mini Project 6
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/add/', views.add_course, name='add_course'),
    path('rounds/new/', views.new_round, name='new_round'),
    path('rounds/<int:pk>/', views.round_detail, name='round_detail'),
    path('rounds/<int:pk>/score/', views.add_score, name='add_score'),
]
