from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Widoki logowania django
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('moje-skorupy/', views.lista_moich_skorup, name='lista-skorup'),
    # Detale konkretnej skorupy (ID to liczba całkowita - int)
    path('skorupa/<int:id_skorupy>/', views.detale_skorupy, name='detale-skorupy'),
    # Edycja konkretnej skorupy
    path('skorupa/<int:id_skorupy>/edycja/', views.edytuj_skorupe, name='edycja-skorupy'),
    # NOWOŚĆ: Link dla biura Dorotki (do wypełniania)
    path('skorupa/<int:id_skorupy>/wypelnij/', views.wypelnij_skorupe, name='wypelnij-skorupe'),
    path('nowa/', views.nowa_skorupa, name='nowa-skorupa'),
    path('skorupa/<int:pk>/usun/', views.usun_skorupe, name='usun-skorupe'),
]