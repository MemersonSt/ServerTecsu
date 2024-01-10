from django.db import models
from apps.products.models import Product


# Create your models here.
class Orden(models.Model):
    codigo_orden = models.CharField('Código de orden', max_length=50, blank=False, null=False)
    fecha_orden = models.DateField('Fecha de orden', auto_now=False, auto_now_add=True)
    estado_orden = models.BooleanField('Estado de orden', default=True)

    class Meta:
        verbose_name = 'Orden'
        verbose_name_plural = 'Ordenes'

    def __str__(self):
        return self.codigo_orden


class OrdenDetalle(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)
    cantidad = models.IntegerField('Cantidad', blank=False, null=False)
    precio = models.DecimalField('Precio', max_digits=10, decimal_places=2, blank=False, null=False)
    total = models.DecimalField('Total', max_digits=10, decimal_places=2, blank=False, null=False)

    class Meta:
        verbose_name = 'OrdenDetalle'
        verbose_name_plural = 'OrdenDetalles'

    def __str__(self):
        return self.orden.codigo_orden

