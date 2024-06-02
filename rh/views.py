from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import path

# Create your views here.
funcionario_logado = False

def home(request):

    if funcionario_logado is False:
        var = {
        'titulo_pag': 'Login'
        }
        return render(request, 'pages/login.html', var)
        
    var = {
        'titulo_pag': 'Home'
    }    
    return render(request, 'pages/home.html', var)

def login(request):
    
    var = {
        'titulo_pag': 'Login'
    }    
    return render(request, 'pages/login.html', var)

def funcionario(request):

    var = {
        'titulo_pag': 'Visualização Funcionario'
    }
    return render(request, 'pages/funcionario.html', var)

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

def cadfuncionario(request):

    var = {
        'titulo_pag': 'Cadastro Funcionario'
    }
    return render(request, 'pages/cadastro/funcionario.html', var)

def cadcargo(request):

    var = {
        'titulo_pag': 'Cadastro Funcionario'
    }
    return render(request, 'pages/cadastro/funcionario.html', var)