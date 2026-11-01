"""
INF601 - Advanced Programming in Python
Ray Bednara
Mini Project 6

URL configuration for golf_tracker project. Routes the admin site and
delegates all other URLs to the scores app.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('scores.urls')),
]
