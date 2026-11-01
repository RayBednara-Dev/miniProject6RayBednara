"""
INF601 - Advanced Programming in Python
Ray Bednara
Mini Project 6
"""
from django import forms

from .models import Course, Round, HoleScore


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'location', 'par', 'holes']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'par': forms.NumberInput(attrs={'class': 'form-control'}),
            'holes': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class RoundForm(forms.ModelForm):
    class Meta:
        model = Round
        fields = ['course', 'date_played', 'notes']
        widgets = {
            'course': forms.Select(attrs={'class': 'form-select'}),
            'date_played': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class HoleScoreForm(forms.ModelForm):
    class Meta:
        model = HoleScore
        fields = ['hole_number', 'strokes']
        widgets = {
            'hole_number': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'strokes': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }
