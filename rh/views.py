from django.shortcuts import render, redirect, get_object_or_404
from django.urls import path, reverse_lazy
from django.views.generic.edit import UpdateView
from .models import Candidato, Funcionario, Cargos, Recrutamento
from .forms import EditarCandidato, EditarCargo, EditarRecrutamento, EditarFuncionario
from django.http import HttpResponse, HttpResponseRedirect
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


def funcionario(request):

    funcionarios = Funcionario.objects.all()
    
    context = {
        'title': 'Visualizar Funcionarios',
        'funcionarios' : funcionarios
    }
    return render(request, 'pages/listar/funcionario.html', context)


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
        nome_func = request.POST.get('nome_completo')
        idade_func = request.POST.get('idade')
        nascimento_func = request.POST.get('data_nascimento')
        cpf_func = request.POST.get('cpf')
        estado_civil_func = request.POST.get('estado_civil')
        cnh_func = request.POST.get('categoria_cnh')

        if nome_func is None:
            return HttpResponse("Nome inválido")

        if nascimento_func is None:
            return HttpResponse("Data inválido")

        funcionario = Funcionario(nome_completo = nome_func, idade=idade_func, data_nascimento = nascimento_func,cpf=cpf_func, estado_civil = estado_civil_func,cnh = cnh_func)
        funcionario.save()
        return HttpResponseRedirect('/funcionarios')

    categorias_cnh = categoriasCNH()
    estados_civis = estado_civil()

    var = {
        'titulo_pag': 'Cadastro Funcionario',
        'categoria_cnh' : categorias_cnh,
        'estados_civis' : estados_civis,
    }
    return render(request, 'pages/cadastro/funcionario.html', var)


def cadcargo(request):
    if request.method == 'POST':
        cargo = request.POST.get('cargo')
        descricao = request.POST.get('descricao')
        departamento = request.POST.get('departamento')
        salario_base = request.POST.get('salario_base')
        requisito_formacao = request.POST.get('requisitos_formacao')
        
        print(requisito_formacao)

        cargo = Cargos(cargo = cargo, descricao=descricao, departamento = departamento,salario_base=salario_base, requisito_formacao = requisito_formacao)
        cargo.save()
        return HttpResponseRedirect('/cargos')

    var = {
        'titulo_pag': 'Cadastro Funcionario',
        'departamentos' : departamentos(),
    }
    return render(request, 'pages/cadastro/cargo.html', var)

def cadrecrutamento(request):
    
    cargos = Cargos.objects.all()
    candidatos = Candidato.objects.all()
    
    if request.method == 'POST':
        nome_candidato = request.POST.get('nome_candidato')
        cargo = request.POST.get('cargo')
        habilidades_tecnicas = request.POST.get('habilidades_tecnicas')
        experiencia_profissional = request.POST.get('experiencia_profissional')
        
        recrutamento = Recrutamento(
            nome_candidato=nome_candidato,
            cargo=cargo,
            habilidades_tecnicas=habilidades_tecnicas,
            experiencia_profissional=experiencia_profissional
        )
        recrutamento.save()
        return HttpResponseRedirect('/recrutamento')
    
    
    context = {
        'titulo_pag': 'Cadastro Recrutamento',
        'cargos' : cargos,
        'candidatos' : candidatos,
    }
    
    return render(request, 'pages/cadastro/recrutamento.html', context)
    
def cadcandidato(request):
    if request.method == 'POST':
        nome_completo = request.POST.get('nome_completo')
        data_nascimento = request.POST.get('data_nascimento')
        escolaridade = request.POST.get('escolaridade')
        contato = request.POST.get('contato')
        endereco_rua = request.POST.get('endereco_rua')
        endereco_numero = request.POST.get('endereco_numero')
        endereco_cidade = request.POST.get('endereco_cidade')
        endereco_estado = request.POST.get('endereco_estado')
        

        candidato = Candidato(nome_completo = nome_completo, data_nascimento=data_nascimento, escolaridade = escolaridade,contato=contato, endereco_rua = endereco_rua,endereco_numero = endereco_numero, endereco_cidade=endereco_cidade, endereco_estado=endereco_estado)
        candidato.save()
        return HttpResponseRedirect('/candidatos')

    context = {
        'title': 'Cadastro de Candidato',
        'ufs': ufs(),
        'escolaridades' : escolaridades()
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


# VIEWS PARA EXCLUSÃO

def deletrecrutamento(request, id_recrutamento):
    
    recrutamento = Recrutamento.objects.get(pk=id_recrutamento)
    recrutamento.delete()
    return HttpResponseRedirect('/recrutamento')