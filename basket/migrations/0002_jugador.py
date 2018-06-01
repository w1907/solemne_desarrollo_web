# Generated by Django 2.0.4 on 2018-06-01 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apodo', models.CharField(max_length=50)),
                ('nacimiento', models.DateField()),
                ('edad', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('estatura', models.PositiveIntegerField(help_text='Indique estatura en centimetros')),
                ('peso', models.PositiveIntegerField(help_text='Indique peso en gramos')),
                ('rut', models.CharField(max_length=8)),
                ('digito_verificador', models.PositiveIntegerField(help_text='Si el digito verificador termina en K reemplace con un 0')),
                ('foto', models.ImageField(upload_to='foto_jugador')),
                ('equipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basket.Equipo')),
            ],
        ),
    ]
