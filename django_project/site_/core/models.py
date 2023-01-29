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

class Veiculo(models.Model):
    marca = models.CharField(max_length=255) 
    modelo = models.CharField(max_length=255)
    ano = models.IntegerField()
    preco = models.CharField(max_length=255)
    
class Financiamento(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    juros = models.DecimalField(max_digits=5,decimal_places=2)
    valor = models.CharField(max_length=255)
    data_inicio = models.DateField()
    data_vencimento = models.DateTimeField()
    class Meta:
        db_table = 'veiculo'
        
    def __str__(self):
        return self.veiculo