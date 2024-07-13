from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import path, reverse_lazy
from django.views.generic.edit import UpdateView
from .models import Candidato, Funcionario, Cargos, Recrutamento
from .forms import FuncionarioForm,CargoForm, RecrutamentoForm, CandidatoForm
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
    return ['','Não Há','A','B','C','D','E','A e B','A e C','A e D','A e E']

def departamentos():
    return ['','TI','Administrativo','Recursos Humanos (RH)','Market','Financeiro']

def estado_civil():
    return ['','Solteiro(a)','Casado(a)','Divorciado(a)','Viuvo(a)']

def escolaridades():
    return ['','Ensino Fundamental','Ensino Médio','Ensino Superior (Incompleto)','Ensino Superior (Completo)']

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
    
    context = {
        'title': 'Visualizar Funcionarios',
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
    recrutamentos = Recrutamento.objects.all()
    
    context = {
        'title': 'Visualizar Recrutamento',
        'recrutamentos' : recrutamentos
    }
    
    return render(request, 'pages/listar/recrutamento.html',context)

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
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cad_funcionario')  # redireciona para uma página de sucesso ou a página desejada
    else:
        form = FuncionarioForm()

    categorias_cnh = categoriasCNH()
    estados_civis = estado_civil()

    var = {
        'titulo_pag': 'Cadastro Funcionario',
        'categoria_cnh' : categorias_cnh,
        'estados_civis' : estados_civis,
        'form': form,
    }
    return render(request, 'pages/cadastro/funcionario.html', var)


def cadcargo(request):
    if request.method == 'POST':
        form = CargoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cad_cargo')  # redireciona para uma página de sucesso ou a página desejada
    else:
        form = CargoForm()

    var = {
        'titulo_pag': 'Cadastro Funcionario',
        'form': form,
    }
    return render(request, 'pages/cadastro/cargo.html', var)

def cadrecrutamento(request):
    if request.method == 'POST':
        form = RecrutamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cad_recrutamento')  # redireciona para uma página de sucesso ou a página desejada
    else:
        form = RecrutamentoForm()

    context = {
        'titulo_pag': 'Cadastro Recrutamento',
        'form': form,
    }
    return render(request, 'pages/cadastro/recrutamento.html', context)

def cadcandidato(request):
    if request.method == 'POST':
        form = CandidatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cad_candidato')  # redireciona para uma página de sucesso ou a página desejada
    else:
        form = CandidatoForm()

    context = {
        'title': 'Cadastro de Candidato',
        'ufs': ufs(),
        'form': form,
    }

    return render(request, 'pages/cadastro/candidato.html', context)


# VIEWS PARA EDIÇÃO


def editcandidato(request, id_candidato):

    escolaridade = escolaridades()
    uf = ufs()

    escolaridade_list = []
    uf_list = []

    candidato = Candidato.objects.get(pk=id_candidato)

    if candidato.escolaridade != "":
        escolaridade_list.append(candidato.escolaridade)

    if candidato.endereco_estado != "":
        uf_list.append(candidato.endereco_estado) 

    if candidato.data_nascimento is not None:
        candidato.data_nascimento = datetime.strftime(candidato.data_nascimento, '%Y-%m-%d')

    form = EditarCandidato(request.POST, instance=candidato)
    
    for escolaridade in escolaridade:
        if not (escolaridade in escolaridade_list):
            escolaridade_list.append(escolaridade)
    
    for uf in uf:
        if not (uf in uf_list):
            uf_list.append(uf)
            
    context = {
        'title' : 'Editar Candidato',
        'ufs' : uf_list,
        'candidato' : candidato,
        'escolaridades' : escolaridade_list
    }

    if form.is_valid():
        print(form)
        form.save()
        return HttpResponseRedirect('/candidatos')
    else:
        print(form.errors)  

    return render(request, 'pages/editar/candidato.html', context)


def editcargo(request, id_cargo):

    cargo_departamento_list = []

    cargos = Cargos.objects.get(pk=id_cargo)
    cargo_departamento_list.append(cargos.departamento)

    form = EditarCargo(request.POST, instance=cargos)
    departamento = departamentos()

    for departamento in departamento:
        if not (departamento in cargo_departamento_list):
            cargo_departamento_list.append(departamento)
    

    context = {
        'departamentos' : cargo_departamento_list,
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

    estado_civis = estado_civil()
    cnh = categoriasCNH()
    estado_civil_list = []
    categoriacnh_list = []
    
    funcionario = Funcionario.objects.get(pk=id_funcionario)
    
    if funcionario.estado_civil != "":
        estado_civil_list.append(funcionario.estado_civil)
        
    if funcionario.cnh !="":
        categoriacnh_list.append(funcionario.cnh)
    
    if funcionario.data_nascimento is not None:
        funcionario.data_nascimento = datetime.strftime(funcionario.data_nascimento, '%Y-%m-%d')
        
    form = EditarFuncionario(request.POST, instance=funcionario)

    for estado_civis in estado_civis:
        if not (estado_civis in estado_civil_list):
            estado_civil_list.append(estado_civis)
            
    for cnh in cnh:
        if not (cnh in categoriacnh_list):
            categoriacnh_list.append(cnh)
            
    context = {
        'title' : 'Editar Funcionário',
        'funcionarios' : funcionario,
        'estados_civis' : estado_civil_list,
        'categorias' : categoriacnh_list,
    }

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/funcionarios')
    else:
        print(form.errors)
    
    return render(request, 'pages/editar/funcionario.html', context)

def editrecrutamento(request, id_recrutamento):
    candidatos_list = []
    cargos_list = []
    
    recrutamento = Recrutamento.objects.get(pk=id_recrutamento)
    
    candidatos_list.append(recrutamento.nome_candidato)
    cargos_list.append(recrutamento.cargo)
    
    candidato = Candidato.objects.all()
    cargo = Cargos.objects.all()
    
    
    for candidato in candidato:
        if not (candidato.nome_completo in candidatos_list):
            candidatos_list.append(candidato.nome_completo)
                    
    for cargo in cargo:
        if not (cargo.cargo in cargos_list):
            cargos_list.append(cargo.cargo)
    
    #for 
    form = EditarRecrutamento(request.POST, instance=recrutamento)
    
    context = {
        'title' : 'Editar Recrutamento',
        'recrutamento' : recrutamento,
        'candidato_recrutado' : candidatos_list,
        'cargo_recrutado' : cargos_list
    }
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/recrutamento')
    else:
        print(form.errors)

    return render(request, 'pages/editar/recrutamento.html', context)
