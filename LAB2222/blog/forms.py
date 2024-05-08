from django import forms

from .models import Player


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ('name', 'number', 'position', 'height', 'weight', 'city','team')
