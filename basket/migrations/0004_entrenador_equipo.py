# Generated by Django 2.0.4 on 2018-06-01 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0003_auto_20180601_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrenador',
            name='equipo',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basket.Equipo'),
        ),
    ]