from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    
    class Meta:
        db_table = 'usuario'
        
    def __str__(self):
        return self.nome

class Carro(models.Model):
    car_model = models.CharField(max_length=100)
    loan_amount = models.FloatField() #valor do veículo
    start_date = models.DateTimeField()
    end_date = models.DateField()
    interest_rate = models.FloatField()
    
    class Meta:
        db_table = 'carro'
    
    def __str__(self):
        return self.car_model