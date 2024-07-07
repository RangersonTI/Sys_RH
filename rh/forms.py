from django.forms.models import ModelForm
from django.db import models
from .models import Candidato, Recrutamento, Funcionario, Cargos
from django import forms

class EditarCandidato(ModelForm):
    #nome_completo = models.CharField(max_length=100)
    #data_nascimento = models.DateField()
    #contato = models.CharField(max_length=100)
    #endereco_rua = models.CharField(max_length=100)
    #endereco_numero = models.CharField(max_length=5)
    #endereco_cidade = models.CharField(max_length=50)
    #endereco_estado = models.CharField(max_length=3)
    #endereco_cep = models.CharField(max_length=10)

    #data_nascimento = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'), input_formats=['%d/%m/%Y'])

    class Meta:
        model = Candidato
        fields = ["nome_completo","data_nascimento","contato","endereco_rua","endereco_numero","endereco_cidade","endereco_estado"]