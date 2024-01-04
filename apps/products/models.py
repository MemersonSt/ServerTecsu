from django.db import models
from apps.base.models import BaseModel

class Producto(BaseModel):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_disponible = models.PositiveIntegerField(default=0)

    # Otros campos específicos que puedas necesitar

    def __str__(self):
        return self.nombre

