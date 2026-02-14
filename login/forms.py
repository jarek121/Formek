from django import forms
from .models import AnkietaSkorupy


class AnkietaForm(forms.ModelForm):
    class Meta:
        model = AnkietaSkorupy
        # Pokazujemy tylko te pola, które Dorotka ma wypełnić
        fields = ['tytul', 'opis', 'data_wygasniecia']
        # Dodajemy polskie etykiety i widgety (np. kalendarz)
        widgets = {
            'data_wygasniecia': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'opis': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'tytul': 'Nazwa ankiety (skorupy)',
            'opis': 'Dodatkowe notatki',
            'data_wygasniecia': 'Kiedy ankieta ma wygasnąć?',
        }