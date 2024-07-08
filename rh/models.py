from django.db import models


class Funcionario(models.Model):
    nome_completo = models.CharField(max_length=100)
    idade = models.IntegerField()
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14)
    estado_civil = models.CharField(max_length=100)
    cnh = models.CharField(max_length=100)


    def __str__(self):
        return f'idade: {self.idade} | data: {self.data_nascimento}'


class Cargos(models.Model):
    cargo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    salario_base = models.DecimalField(max_digits=10, decimal_places=2)
    requisito_formacao = models.CharField(max_length=100)


    def __str__(self):
        return f'cargo: {self.cargo} | departamento: {self.departamento}'

class Candidato(models.Model):
    nome_completo = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    contato = models.CharField(max_length=100)
    endereco_rua = models.CharField(max_length=100)
    endereco_numero = models.CharField(max_length=5)
    endereco_cidade = models.CharField(max_length=50)
    endereco_estado = models.CharField(max_length=3)
    endereco_cep = models.CharField(max_length=10)


    def __str__(self):
        return f'nome_completo: {self.nome_completo} | contato: {self.contato}'

class Recrutamento(models.Model):
    nome_candidato = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    escolaridade = models.CharField(max_length=100)
    habilidades_tecnicas = models.CharField(max_length=100)
    experiencia_profissional = models.CharField(max_length=100)


    def __str__(self):
        return f'nome_candidato: {self.nome_candidato} | cargo: {self.cargo}'
