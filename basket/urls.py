from django.urls import path
from basket import views


urlpatterns = [
    #path('', views.index, name="player"),
    path('', views.inicio, name="inicio"),
    path('agregar', views.AgregarEquipo, name="agregar_equipo"),
    path('lista', views.ListaJugadores, name="listar_jugadores"),
    #path('add', views.add, name="player_add"),
    #path('view/<int:player_id>', views.detail, name="player_detail"),
]