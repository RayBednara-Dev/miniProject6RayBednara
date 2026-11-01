"""
INF601 - Advanced Programming in Python
Ray Bednara
Mini Project 6
"""
from django.conf import settings
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    par = models.PositiveSmallIntegerField(default=72)
    holes = models.PositiveSmallIntegerField(default=18)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Round(models.Model):
    player = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rounds'
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='rounds')
    date_played = models.DateField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_played']

    def __str__(self):
        return f'{self.player} at {self.course} on {self.date_played}'

    @property
    def total_score(self):
        total = self.hole_scores.aggregate(models.Sum('strokes'))['strokes__sum']
        return total or 0

    @property
    def to_par(self):
        return self.total_score - self.course.par


class HoleScore(models.Model):
    round = models.ForeignKey(Round, on_delete=models.CASCADE, related_name='hole_scores')
    hole_number = models.PositiveSmallIntegerField()
    strokes = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['hole_number']
        unique_together = ('round', 'hole_number')

    def __str__(self):
        return f'Hole {self.hole_number}: {self.strokes} strokes'
