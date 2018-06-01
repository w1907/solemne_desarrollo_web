from django.contrib import admin
from basket.models import Equipo, Jugador, Entrenador

# Register your models here.

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'thumbnail',)


@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'apodo', 'edad', 'thumbnail',)


@admin.register(Entrenador)
class EntrenadorAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'apodo', 'edad', 'email',)