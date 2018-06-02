from django import forms
from basket.models import Equipo, Jugador, Entrenador

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


class EntrenadorForm(forms.ModelForm):

	class Meta:
		model = Entrenador
		fields = [
			'nombre',
			'apodo',
			'edad',
			'email',
			'rut',
			'digito_verificador',
			'equipo',
		]
		labels = {
			'nombre': 'Nombre del Entrenador',
			'apodo': 'Apodo del Entrenador',
			'edad': 'Edad del Entrenador',
			'email': 'Email del Entrenador',
			'rut': 'RUT del Entrenador',
			'digito_verificador': 'Digito verificador del Entrenador',
			'equipo': 'Equipo del Entrenador',
		}


class JugadorForm(forms.ModelForm):

	class Meta:
		model = Jugador
		fields = [
			'nombre',
			'apodo',
			'nacimiento',
			'edad',
			'email',
			'estatura',
			'peso',
			'rut',
			'digito_verificador',
			'foto',
			'posicion',
			'equipo',
		]
		labels = {
			'nombre': 'Nombre del Jugador',
			'apodo': 'Apodo del Jugador',
			'nacimiento': 'Fecha de nacimiento',
			'edad': 'Edad del Jugador',
			'email': 'Email del Jugador',
			'estatura': 'Estatura del Jugador',
			'peso': 'Peso del Jugador',
			'rut': 'RUT del Jugador',
			'digito_verificador': 'Digito verificador del Jugador',
			'foto': 'Foto del Jugador',
			'posicion': 'Posicion del Jugador',
			'equipo': 'Equipo del Jugador:',
		}