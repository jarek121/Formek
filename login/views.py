from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import AnkietaSkorupy
from .forms import AnkietaForm
from django.views.decorators.http import require_POST
from .models import Skorupa


#Widok dashboard
@login_required
def dashboard(request):
    return render(request,
        'registration/dashboard.html', 
        {'section': 'dashboard'}
    )

# wyciągnięcie skorup zalogowanego twórcy

@login_required
def lista_moich_skorup(request):
    # Wyciągamy z bazy tylko te ankiety, gdzie tworca to osoba zalogowana
    # To jest ten moment, gdzie user widzi SWOJE rzeczy
    moje_ankiety = AnkietaSkorupy.objects.filter(tworca=request.user).order_by('-data_utworzenia')
    return render(request, 'registration/moje_skorupy.html', {'skorupy': moje_ankiety})



# 1. Detale skorupy
def detale_skorupy(request, id_skorupy):
    # Szukamy konkretnej skorupy po ID
    skorupa = get_object_or_404(AnkietaSkorupy, id=id_skorupy)
    return render(request, 'registration/detale_skorupy.html', {'skorupa': skorupa})

# 2. Widok dla biura (Wypełnianie)
def wypelnij_skorupe(request, id_skorupy):
    skorupa = get_object_or_404(AnkietaSkorupy, id=id_skorupy)
    
    # Wykorzystujemy Twoją logikę blokady czasu
    if not skorupa.czy_mozna_wypelnic():
        return render(request, 'registration/skorupa_zamknieta.html', {'skorupa': skorupa})
    
    # Jeśli wszystko OK, pokazujemy formularz ankiety
    return render(request, 'registration/formularz_ankiety.html', {'skorupa': skorupa})

# 3. Edycja skorupy (na razie tylko podgląd)
def edytuj_skorupe(request, id_skorupy):
    skorupa = get_object_or_404(AnkietaSkorupy, id=id_skorupy)
    # Tutaj w przyszłości dodamy obsługę formularza POST
    return render(request, 'registration/edycja_skorupy.html', {'skorupa': skorupa})

@login_required
def nowa_skorupa(request):
    if request.method == 'POST':
        form = AnkietaForm(request.POST)
        if form.is_valid():
            ankieta = form.save(commit=False)
            ankieta.tworca = request.user  # Automatycznie przypisujemy zalogowanego user'a
            ankieta.save()
            return redirect('lista-skorup')
    else:
        form = AnkietaForm()
    
    return render(request, 'registration/formularz_edycji.html', {'form': form, 'tytul_strony': 'Nowa Skorupa'})


@require_POST
@login_required # Warto dodać, żeby tylko zalogowani mogli usuwać
def usun_skorupe(request, pk):
    # Używamy AnkietaSkorupy, bo tak nazywa się Twój główny model
    # Używamy pola 'tworca', bo tak zdefiniowałeś użytkownika w tym modelu
    AnkietaSkorupy.objects.filter(id=pk, tworca=request.user).delete()
    
    return redirect('lista-skorup')