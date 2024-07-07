from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import path, reverse_lazy
from django.views.generic.edit import UpdateView
from .models import Candidato, Funcionario, Cargos, Recrutamento
from .forms import EditarCandidato
from django.http import HttpResponseRedirect
from datetime import datetime

# Create your views here.
usuario_p = 'admin'
senha_p = 'admin'

# OUTRAS FUNÇÕES

def ufs():
    return ['','AC','AL','AM','AP','BA','CE','DF','ES','GO','MA','MG','MS','MT','PA','PB','PE','PI','PR','RJ','RN','RO','RR','RS','SC','SE','SP','TO']

def categoriasCNH():
    return ['Não há','A','B','C','D','E','A e B','A e C','A e D','A e E']

# VIEWS DE LISTAGEM / LOGIN / HOME

def home(request):
    if not request.session.get('funcionario_logado', False):
        return redirect('login')

    var = {
        'titulo_pag': 'Home'
    }
    return render(request, 'pages/home.html', var)

def login(request):
    var = {
        'titulo_pag': 'Login'
    }

    if request.method == 'POST':
        usuario = request.POST.get('input_usuario')
        senha = request.POST.get('input_senha')

        usuario_valido = (usuario == usuario_p)
        senha_valido = (senha == senha_p)

        if usuario_valido and senha_valido:
            request.session['funcionario_logado'] = True
            return redirect('home')

    return render(request, 'pages/login.html', var)

#@login_required


def funcionario(request):
    var = {
        'titulo_pag': 'Visualização Funcionario'
    }
    return render(request, 'pages/listar/funcionario.html', var)

#@login_required
def cargo(request):
    var = {
        'titulo_pag': 'Visualização Cargos'
    }
    return render(request, 'pages/listar/cargo.html', var)

def recrutamento(request):
    var = {
        'titulo_pag': 'Recrutamento'
    }
    return render(request, 'pages/listar/recrutamento.html')

#@login_required
def candidatos(request):
    
    candidatos = Candidato.objects.all()
    print(candidatos)
    
    context = {
        'title' : 'Visualizar Candidatos',
        'candidatos' : candidatos
    }
    
    return render(request, 'pages/listar/candidato.html', context)


# VIEWS PARA CADASTROS


def cadfuncionario(request):
    
    estado_civil = ['Solteiro(a)','Casado(a)','Divorciado(a)','Viuvo(a)']
    categorias_cnh = categoriasCNH()

    var = {
        'titulo_pag': 'Cadastro Funcionario',
        'categoria_cnh' : categorias_cnh,
        'estados_civis' : estado_civil
    }
    return render(request, 'pages/cadastro/funcionario.html', var)

def cadcargo(request):
    var = {
        'titulo_pag': 'Cadastro Funcionario'
    }
    return render(request, 'pages/cadastro/cargo.html', var)

def cadrecrutamento(request):
    
    return render(request, 'pages/cadastro/recrutamento.html')

def cadcandidato(request):
    
    list_uf = ufs()
    
    context = {
        'title' : 'Cadastro de Candidato',
        'ufs' : list_uf
    }

    return render(request, 'pages/cadastro/candidato.html', context)


# VIEWS PARA EDIÇÃO


def editcandidato(request, id_usuario):
    print("\n\n"+request.method+"\n\n")

    candidatos = Candidato.objects.get(pk=id_usuario)
    candidatos.data_nascimento = datetime.strftime(candidatos.data_nascimento, '%Y-%m-%d')
    form = EditarCandidato(request.POST, instance=candidatos)
    lista_uf = ufs()

    context = {
        'candidato' : candidatos,
        'ufs' : lista_uf,
        'form' : form
    }

    if form.is_valid():
        print("\n\nSalvo Savo Salvo\n\n")
        form.save()
        return HttpResponseRedirect('/candidatos')
    else:
        print(form.errors)  

    return render(request, 'pages/editar/candidato.html', context)




    #if request.method == 'GET':
    #    
    #
    #if request.method == 'POST':
#
#
    #    if form.is_valid():
    #        candidato = Candidato.objects.get(pk=id_usuario)
    #        candidato.nome_completo = form.cleaned_data['nome_completo']
    #        candidato.data_nascimento = form.cleaned_data['data_nascimento']
    #        candidato.contato = form.cleaned_data['contato']
    #        candidato.endereco_rua = form.cleaned_data['endereco_rua']
    #        candidato.endereco_numero = form.cleaned_data['endereco_numero']
    #        candidato.endereco_cidade = form.cleaned_data['endereco_cidade']
    #        candidato.endereco_estado = form.cleaned_data['endereco_estado']
    #        candidato.save()