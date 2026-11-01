"""
INF601 - Advanced Programming in Python
Ray Bednara
Mini Project 6
"""
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CourseForm, RegisterForm, RoundForm, RoundScoresForm
from .models import Course, HoleScore, Round


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created. Welcome to Golf Tracker!')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def home(request):
    rounds = request.user.rounds.all()[:5]
    return render(request, 'scores/home.html', {'rounds': rounds})


@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'scores/course_list.html', {'courses': courses})


@login_required
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course added.')
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'scores/course_form.html', {'form': form})


@login_required
def new_round(request):
    if request.method == 'POST':
        form = RoundForm(request.POST)
        if form.is_valid():
            new_round_obj = form.save(commit=False)
            new_round_obj.player = request.user
            new_round_obj.save()
            messages.success(request, 'Round started. Enter your scores below.')
            return redirect('round_detail', pk=new_round_obj.pk)
    else:
        form = RoundForm()
    return render(request, 'scores/round_form.html', {'form': form})


@login_required
def round_detail(request, pk):
    round_obj = get_object_or_404(Round, pk=pk, player=request.user)
    scores_by_hole = {s.hole_number: s.strokes for s in round_obj.hole_scores.all()}
    hole_rows = [
        (hole, scores_by_hole.get(hole))
        for hole in range(1, round_obj.course.holes + 1)
    ]

    score_form = RoundScoresForm(holes=round_obj.course.holes, scores=scores_by_hole)

    return render(request, 'scores/round_detail.html', {
        'round': round_obj,
        'hole_rows': hole_rows,
        'score_form': score_form,
    })


@login_required
def add_score(request, pk):
    round_obj = get_object_or_404(Round, pk=pk, player=request.user)
    if request.method == 'POST':
        form = RoundScoresForm(request.POST, holes=round_obj.course.holes)
        if form.is_valid():
            for hole in range(1, round_obj.course.holes + 1):
                strokes = form.cleaned_data.get(f'hole_{hole}')
                if strokes:
                    HoleScore.objects.update_or_create(
                        round=round_obj, hole_number=hole, defaults={'strokes': strokes}
                    )
                else:
                    HoleScore.objects.filter(round=round_obj, hole_number=hole).delete()
            messages.success(request, 'Scorecard saved.')
    return redirect('round_detail', pk=round_obj.pk)


@login_required
def stats(request):
    rounds = list(request.user.rounds.select_related('course'))
    rounds_with_scores = [r for r in rounds if r.total_score]

    best_round = min(rounds_with_scores, key=lambda r: r.total_score, default=None)
    average_score = None
    if rounds_with_scores:
        average_score = sum(r.total_score for r in rounds_with_scores) / len(rounds_with_scores)

    return render(request, 'scores/stats.html', {
        'rounds_played': len(rounds),
        'best_round': best_round,
        'average_score': average_score,
    })
