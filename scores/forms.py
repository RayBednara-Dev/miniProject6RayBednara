"""
INF601 - Advanced Programming in Python
Ray Bednara
Mini Project 6
"""
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Course, Round


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


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


class RoundScoresForm(forms.Form):
    """Builds one strokes field per hole so a whole round can be entered at once."""

    def __init__(self, *args, holes=18, scores=None, **kwargs):
        super().__init__(*args, **kwargs)
        scores = scores or {}
        for hole in range(1, holes + 1):
            self.fields[f'hole_{hole}'] = forms.IntegerField(
                label=f'Hole {hole}',
                required=False,
                min_value=1,
                initial=scores.get(hole),
                widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            )
