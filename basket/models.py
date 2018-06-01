from django.db import models
from django.utils.safestring import mark_safe

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
