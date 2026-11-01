"""
INF601 - Advanced Programming in Python
Ray Bednara
Mini Project 6
"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Course


@login_required
def home(request):
    rounds = request.user.rounds.all()[:5]
    return render(request, 'scores/home.html', {'rounds': rounds})


@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'scores/course_list.html', {'courses': courses})
