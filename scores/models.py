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
    score = models.PositiveSmallIntegerField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_played']

    def __str__(self):
        return f'{self.player} at {self.course} on {self.date_played}'

    @property
    def to_par(self):
        if self.score is None:
            return None
        return self.score - self.course.par
