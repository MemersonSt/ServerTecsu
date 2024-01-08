from django.db import models
from apps.Users.models import User, Estudents


# Create your models here.
class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    numero_identidad = models.CharField(max_length=20)
    code_student = models.CharField(max_length=20)
    amount = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction: {self.id} - {self.numero_identidad} - {self.amount} - {self.date}"
