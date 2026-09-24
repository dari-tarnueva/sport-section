from django import forms
from .models import Trainer, Section, Athlete, Schedule, Subscription


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['full_name', 'specialization']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-input'}),
            'specialization': forms.TextInput(attrs={'class': 'form-input'}),
        }


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['name', 'description', 'trainer']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-input', 'rows': 4}),
            'trainer': forms.Select(attrs={'class': 'form-input'}),
        }


class AthleteForm(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = ['full_name', 'birth_date', 'phone']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-input'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'phone': forms.TextInput(attrs={'class': 'form-input'}),
        }


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['section', 'date', 'time', 'location']
        widgets = {
            'section': forms.Select(attrs={'class': 'form-input'}),
            'date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-input', 'type': 'time'}),
            'location': forms.TextInput(attrs={'class': 'form-input'}),
        }


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['athlete', 'type', 'start_date', 'end_date']
        widgets = {
            'athlete': forms.Select(attrs={'class': 'form-input'}),
            'type': forms.TextInput(attrs={'class': 'form-input'}),
            'start_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
        }