from django.db import models
from productosapi.models import Productos

# Create your models here.

class Venta(models.Model):
    fecha =  models.DateTimeField(auto_now_add=True, null=True)
    detalle = models.CharField(max_length=300, verbose_name='Detalle del pedido',null=True)
    producto = models.ForeignKey(Productos,on_delete=models.CASCADE,verbose_name='Producto', null=True)
    cantidad = models.IntegerField(null=True)


