from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    data = models.DateField()
    estado_civil = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return f'idade: {self.idade} | data: {self.data}'

class Cargos(models.Model):
    cargo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    salarioBase = models.DecimalField(max_digits=10, decimal_places=2)
    requisitoDeformacao = models.CharField(max_length=100)

    def __str__(self):
        return f'cargo: {self.cargo} | departamento: {self.departamento}'