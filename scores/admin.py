"""
INF601 - Advanced Programming in Python
Ray Bednara
Mini Project 6
"""
from django.contrib import admin

from .models import Course, Round


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'par', 'holes', 'created_at')
    search_fields = ('name', 'location')
    list_filter = ('holes',)


@admin.register(Round)
class RoundAdmin(admin.ModelAdmin):
    list_display = ('player', 'course', 'date_played', 'score', 'to_par')
    list_filter = ('course', 'date_played')
    search_fields = ('player__username', 'course__name')
    date_hierarchy = 'date_played'
