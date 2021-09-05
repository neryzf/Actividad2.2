from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Cliente(models.Model):
    doc = (
    ('D','DPI'),
    ('C','CEDULA'),

    )
    nombre =models.CharField(max_length=50)
    apellido =models.CharField(max_length=50)
    direccion =models.CharField(max_length=200)
    nacimiento =models.DateField()
    tipo = models.ForeignKey(
        'TipoCliente',
        on_delete= models.CASCADE,
        default=1,
        )
    documento = models.CharField(
        max_length=20,
        choices=doc,
        default="D")
    creacion =models.DateField(auto_now_add=True)
    actualizacion =models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.nombre,self.apellido)

class TipoCliente(models.Model):
    tipo =models.CharField(max_length=10)
    creacion =models.DateField(auto_now_add=True)
    actualizacion =models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s ' % (self.tipo)

class Venta(models.Model):
    cliente = models.ManyToManyField(Cliente)
    fecha = models.DateField()
    def __str__(self):
        return '%s ' % (self.fecha)