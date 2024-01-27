from django.db import models
from apps.Users.models import User, Students


# Create your models here.
class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    cedula_representante = models.CharField(max_length=20)
    cedula_estudiante = models.CharField(max_length=20)
    amount = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction: {self.id} - {self.cedula_representante} - {self.amount} - {self.date}"
