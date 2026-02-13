from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username = cd['username'], password = cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Zostałeś zalogowany')
                else: 
                    return HttpResponse('Konto zablokowane')
            else:
                return HttpResponse('Niepoprawne dane')
    else:
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})       