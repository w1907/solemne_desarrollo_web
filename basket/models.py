from django.db import models
from django.utils.safestring import mark_safe
from basket.defines import Posicion_Jugador_Opcion

# Create your models here.

class Equipo(models.Model):
	nombre = models.CharField(max_length = 50)
	descripcion = models.TextField()
	logo = models.ImageField(upload_to = 'logo_equipo')


	def thumbnail(self):
		if self.logo:
			return mark_safe('<img src="%s" widght=80 height=80/>' % self.logo.url)
		else:
			return '(no imagen)'
		thumbnail.short_description = 'Thumb'


	def __str__(self):
		return self.nombre


class Jugador(models.Model):
	nombre = models.CharField(max_length = 50)
	apodo = models.CharField(max_length = 50)
	nacimiento = models.DateField()
	edad = models.PositiveIntegerField()
	email = models.EmailField()
	estatura = models.PositiveIntegerField(help_text = 'Indique estatura en centimetros')
	peso = models.PositiveIntegerField(help_text = 'Indique peso en libras')
	rut = models.CharField(max_length = 8)
	digito_verificador = models.PositiveIntegerField(help_text = 'Si el digito verificador termina en K, reemplace con un 0')
	foto = models.ImageField(upload_to = 'foto_jugador')
	posicion = models.CharField(max_length=60, choices = Posicion_Jugador_Opcion, default = 'Base')
	equipo = models.ForeignKey('Equipo', null = True, blank = True, on_delete = models.CASCADE)
	

	def thumbnail(self):
		if self.foto:
			return mark_safe('<img src="%s" widght=80 height=80/>' % self.foto.url)
		else:
			return '(no imagen)'
		thumbnail.short_description = 'Thumb'


	def fullRut(self):
		return '{}-{}' . format(self.rut, self.digito_verificador)


	def __str__(self):
		return self.nombre


class Entrenador(models.Model):
	nombre = models.CharField(max_length = 50)
	apodo = models.CharField(max_length = 50)
	edad = models.PositiveIntegerField()
	email = models.EmailField()
	rut = models.CharField(max_length = 8)
	digito_verificador = models.PositiveIntegerField(help_text = 'Si el digito verificador termina en k, reemplace con un 0')
	equipo = models.OneToOneField('Equipo', null = True, blank = True, on_delete = models.CASCADE)


	def fullRut(self):
		return '{}-{}' . format(self.rut, self.digito_verificador)


	def __str__(self):
		return self.nombre

class Nomina(models.Model):
	nombre = models.CharField(max_length = 50)
	fecha = models.DateField()
	jugadores = models.ForeignKey('Jugador', null = True, blank = True, on_delete = models.CASCADE)