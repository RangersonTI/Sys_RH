from django import forms
from .models import Candidato, Recrutamento, Funcionario, Cargos

class EditarCandidato(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = ['nome_completo', 'data_nascimento', 'contato', 'endereco_numero', 'endereco_estado', 'endereco_cep']