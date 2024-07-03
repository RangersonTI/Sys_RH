from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    data = models.DateField()
    estado_civil = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return f'idade: {self.idade} | data: {self.data}'

