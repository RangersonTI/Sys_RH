from django.db import models

class rh(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.TextField()
    data= models.DateField()
