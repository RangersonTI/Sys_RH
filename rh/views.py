from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import path, reverse_lazy
from django.views.generic.edit import UpdateView
from .models import Candidato, Funcionario, Cargos, Recrutamento
from .forms import EditarCandidato, EditarCargo, EditarRecrutamento, EditarFuncionario
from django.http import HttpResponseRedirect
from datetime import datetime

# Create your views here.
usuario_p = 'admin'
senha_p = 'admin'

# OUTRAS FUNÇÕES

def ufs():
    return ['','AC','AL','AM','AP','BA','CE','DF','ES','GO','MA','MG','MS','MT','PA','PB','PE','PI','PR','RJ','RN','RO','RR','RS','SC','SE','SP','TO']

def categoriasCNH():
    return ['nao_ha','A','B','C','D','E','A e B','A e C','A e D','A e E']

def departamentos():
    return ['','TI','Administrativo','Recursos Humanos (RH)','Market','Financeiro']

def estado_civil():
    return ['Solteiro(a)','Casado(a)','Divorciado(a)','Viuvo(a)']
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

    funcionarios = Funcionario.objects.all()
    
    
    #for funcionario in funcionarios:
    #    funcionario.data_nasicimento = datetime.strftime(funcionario.data_nasicimento, '%Y-%m-%d')
        
    print(f"\n\n{funcionario}\n\n")

    context = {
        'title': 'Vizualizar Funcionarios',
        'funcionarios' : funcionarios
    }
    return render(request, 'pages/listar/funcionario.html', context)

#@login_required
def cargo(request):
    cargos = Cargos.objects.all()
    print(f"\n\n{cargos}\n\n")
    
    context = {
        'cargos': cargos,
        'title' : 'Visualizar Cargos'
    }
    
    return render(request, 'pages/listar/cargo.html', context)

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
    
    categorias_cnh = categoriasCNH()

    var = {
        'titulo_pag': 'Cadastro Funcionario',
        'categoria_cnh' : categorias_cnh,
        'estados_civis' : estado_civil()
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
    
    context = {
        'title' : 'Cadastro de Candidato',
        'ufs' : ufs(),
    }

    return render(request, 'pages/cadastro/candidato.html', context)


# VIEWS PARA EDIÇÃO


def editcandidato(request, id_candidato):
    print("\n\n"+request.method+"\n\n")

    candidato = Candidato.objects.get(pk=id_candidato)
    candidato.data_nascimento = datetime.strftime(candidatos.data_nascimento, '%Y-%m-%d')
    form = EditarCandidato(request.POST, instance=candidato)
    context = {
        'ufs' : ufs(),
        'candidato' : candidato,
        'form' : form
    }

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/candidatos')
    else:
        print(form.errors)  

    return render(request, 'pages/editar/candidato.html', context)


def editcargo(request, id_cargo):

    cargos = Cargos.objects.get(pk=id_cargo)
    form = EditarCargo(request.POST, instance=cargos)
    
    print(cargos)
    context = {
        'departamentos' : departamentos(),
        'title' : 'Editar Cargo',
        'cargo' : cargos
    }

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/cargos')
    else:
        print(form.errors)
    
    return render(request,'pages/editar/cargo.html', context)

def editfuncionario(request, id_funcionario):
    
    funcionario = Funcionario.objects.get(pk=id_funcionario)
    form = EditarFuncionario(request.POST, instance=funcionario)
    
    print(funcionario)
    
    context = {
        'title' : 'Editar Funcionário',
        'funcionarios' : funcionario,
        'estados_civis' : estado_civil(),
        'categorias' : categoriasCNH(),
    }
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/funcionarios')
    else:
        print(form.errors)
        
    return render(request, 'pages/editar/funcionario.html', context)