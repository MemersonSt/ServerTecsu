from django.db import models
from apps.shoppingCart.models import Orden, OrdenDetalle


# Create your models here.
class Compra(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    orden_detalle = models.ForeignKey(OrdenDetalle, on_delete=models.CASCADE)
    fecha_compra = models.DateField('Fecha de compra', auto_now=False, auto_now_add=True)
    estado_compra = models.BooleanField('Estado de compra', default=True)

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'

    def __str__(self):
        return self.orden.codigo_orden

