from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import path

# Create your views here.
funcionario_logado = False

def home(request):

    #if funcionario_logado is False:
    #    var = {
    #    'titulo_pag': 'Login'
    #    }
    #    return render(request, 'pages/login.html', var)
        
    var = {
        'titulo_pag': 'Home'
    }    
    return render(request, 'pages/home.html', var)

def login(request):
    usuario_p = 'admin'
    senha_p = 'admin'

    usuario = request.POST.get('input_usuario')
    senha = request.POST.get('input_senha')

    usuario_valido = (usuario == usuario_p)
    senha_valido = (senha == senha_p)
    
    print(f"Usuario: {usuario} e Senha: {senha}")
    print(f"Usuario_p: {usuario_p} e Senha: {senha_p}")
    #print(f"Usuario: {usuario_valido} e Senha: {senha_valido}")

    if usuario_valido and senha_valido:
        print("Simbora")
        funcionario_logado = True
        return redirect('home')

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