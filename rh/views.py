from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import path

# Create your views here.
usuario_p = 'admin'
senha_p = 'admin'

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

@login_required
def funcionario(request):
    var = {
        'titulo_pag': 'Visualização Funcionario'
    }
    return render(request, 'pages/funcionario.html', var)

@login_required
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

@login_required
def cadfuncionario(request):
    var = {
        'titulo_pag': 'Cadastro Funcionario'
    }
    return render(request, 'pages/cadastro/funcionario.html', var)

@login_required
def cadcargo(request):
    var = {
        'titulo_pag': 'Cadastro Funcionario'
    }
    return render(request, 'pages/cadastro/cargo.html', var)