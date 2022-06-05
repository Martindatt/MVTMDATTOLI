from django.db import models

# Create your models here.

class Cliente(models.Model):

    nombreC = models.CharField(max_length=40)
    tipo_cli = models.CharField(max_length=40)
    rama = models.CharField(max_length=40)


class Proveedor (models.Model):

    nombreP = models.CharField(max_length=40)
    codigoprov = models.IntegerField()
    tipo_prov = models.CharField(max_length=40)
    rama = models.CharField(max_length=40)

class Personal (models.Model):

    nombreU = models.CharField(max_length=40)
    sector = models.CharField(max_length=40)
    rol = models.CharField(max_length=40)
