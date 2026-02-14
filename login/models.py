from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class AnkietaSkorupy(models.Model):
    # Kto to stworzył? (Relacja do tabeli User)
    tworca = models.ForeignKey(User, on_delete=models.PROTECT, related_name='moje_ankiety')
    
    # Podstawowe info
    tytul = models.CharField(max_length=200)
    opis = models.TextField(blank=True)
    
    # Daty (auto_now_add ustawia datę tylko raz przy stworzeniu)
    data_utworzenia = models.DateTimeField(auto_now_add=True)
    data_edycji = models.DateTimeField(auto_now=True)
    
    # Termin ważności (może być pusty - null=True)
    data_wygasniecia = models.DateTimeField(null=True, blank=True)
    
    # Status
    czy_aktywna = models.BooleanField(default=True)

    def czy_mozna_wypelnic(self):
        # Porównujemy aktualny czas (timezone.now) z datą wygaśnięcia
        if self.data_wygasniecia and timezone.now() > self.data_wygasniecia:
            return False
        return self.czy_aktywna