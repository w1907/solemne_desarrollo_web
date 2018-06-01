from django.contrib import admin
from basket.models import Equipo

# Register your models here.

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'thumbnail',)