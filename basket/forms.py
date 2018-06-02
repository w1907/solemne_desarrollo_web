from django import forms
from basket.models import Equipo

class EquipoForm(forms.ModelForm):

	class Meta:
		model = Equipo
		fields = [
			'nombre',
			'descripcion',
			'logo',
		]
		labels = {
			'nombre': 'Nombre del Equipo',
			'descripcion': 'Descripcion del Equipo',
			'logo': 'Logo del Equipo',
		}