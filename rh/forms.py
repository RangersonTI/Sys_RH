from django.forms.models import ModelForm
from django.db import models
from .models import Candidato, Recrutamento, Funcionario, Cargos
from django import forms

class EditarCandidato(ModelForm):
    class Meta:
        model = Candidato
        fields = ["nome_completo","escolaridade","data_nascimento","contato","endereco_rua","endereco_numero","endereco_cidade","endereco_estado"]

class EditarCargo(ModelForm):
    class Meta:
        model = Cargos
        fields = "__all__"

class EditarRecrutamento(ModelForm):
    class Meta:
        model = Recrutamento
        fields = "__all__"
 
class EditarFuncionario(ModelForm):
    class Meta:
        model = Funcionario
        fields = "__all__"