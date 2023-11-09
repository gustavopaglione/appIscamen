from django.db import models

class RECP_PUPA(models.Model):
    fecha = models.DateField()
    horarios = models.TimeField()
    temperatura = models.FloatField()
    litros = models.IntegerField()
    lotes = models.IntegerField()

class Produccion(models.Model):
    fecha = models.DateField()
    lotes = models.IntegerField()
    millones_procesados = models.IntegerField()
    cantidad_torres = models.IntegerField()

class Liberacion(models.Model):
    fecha_horarios = models.DateTimeField()
    sector = models.CharField(max_length=50)
    temp_humedad_entrega_cajas = models.FloatField()
    temp_humedad_ingreso_sector_liberacion = models.FloatField()
    millones_liberados = models.IntegerField()
