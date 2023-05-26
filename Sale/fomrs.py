from django import forms
from .models import Rezerwacje

class RezerwacjaForm(forms.ModelForm):
    class Meta:
        model = Rezerwacje
        fields = [
          'sala',
          'catering',
          'wyposazenie',
          'poczatek_wynajmu',
          'koniec_wynajmu'
        ]