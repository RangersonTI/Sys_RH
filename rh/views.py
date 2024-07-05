from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import path

# Create your views here.
usuario_p = 'admin'
senha_p = 'admin'


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
    return render(request, 'pages/funcionario.html', var)

#@login_required
def cargo(request):
    var = {
        'titulo_pag': 'Visualização Cargos'
    }
    return render(request, 'pages/cargo.html', var)

def recrutamento(request):
    var = {
        'titulo_pag': 'Recrutamento'
    }
    return render(request, 'pages/recrutamento.html')

#@login_required
def candidatos(request):
    
    return render(request, 'pages/candidato.html')


# VIEWS PARA CADASTROS


def cadfuncionario(request):
    
    estado_civil = ['Solteiro(a)','Casado(a)','Divorciado(a)','Viuvo(a)']
    categorias_cnh = ['Não há','A','B','C','D','E','A e B','A e C','A e D','A e E']

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
    
    list_uf = ['selecione uma opcao','AC','AL','AM','AP','BA','CE','DF','ES','GO','MA','MG','MS','MT','PA','PB','PE','PI','PR','RJ','RN','RO','RR','RS','SC','SE','SP','TO']
    
    context = {
        'title' : 'Cadastro de Candidato',
        'ufs' : list_uf
    }

    return render(request, 'pages/cadastro/candidato.html', context)