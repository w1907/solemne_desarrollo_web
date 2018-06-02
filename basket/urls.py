from django.urls import path
from basket import views


urlpatterns = [
    #path('', views.index, name="player"),
    path('', views.inicio, name="inicio"),
    path('agregar_equipo', views.AgregarEquipo, name="agregar_equipo"),
    path('agregar_jugador', views.AgregarJugador, name="agregar_jugador"),
    path('agregar_entrenador', views.AgregarEntrenador, name="agregar_entrenador"),
    path('editar_equipo/<int:equipo_id>', views.EditarEquipo, name="editar_equipo"),
    path('editar_jugador/<int:jugador_id>', views.EditarJugador, name="editar_jugador"),
    path('editar_entrenador/<int:entrenador_id>', views.EditarEntrenador, name="editar_entrenador"),
    path('eliminar_equipo/<int:equipo_id>', views.EliminarEquipo, name="eliminar_equipo"),
    #path('eliminar_jugador', views.EliminarJugador, name="eliminar_jugador"),
    #path('eliminar_entrenador', views.EliminarEntrenador, name="eliminar_entrenador"),
    path('lista_jugador', views.ListaJugadores, name="listar_jugadores"),
    path('lista_equipo', views.ListaEquipos, name="listar_equipos"),
    path('lista_entrenador', views.ListaEntrenadores, name="listar_entrenadores"),
    #path('add', views.add, name="player_add"),
    #path('view/<int:player_id>', views.detail, name="player_detail"),
]