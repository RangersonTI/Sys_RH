from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import path

# Create your views here.
funcionario_logado = False
usuario_p = 'admin'
senha_p = 'admin'

def validar_login():
    if funcionario_logado is False:
        print(f"Usuario logado: \n{funcionario_logado}\n")
        #var = {
        #'titulo_pag': 'Login'
        #}
        return redirect('login')

def home(request):

    validar_login()
    var = {
        'titulo_pag': 'Home'
    }    
    return render(request, 'pages/home.html', var)
def login(request):
    var = {
        'titulo_pag': 'Login'
    }
    
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

    return render(request, 'pages/login.html', var)

def funcionario(request):

    validar_login()
    var = {
        'titulo_pag': 'Visualização Funcionario'
    }
    return render(request, 'pages/funcionario.html', var)

def cargo(request):

    validar_login()
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

    validar_login()
    var = {
        'titulo_pag': 'Cadastro Funcionario'
    }
    return render(request, 'pages/cadastro/funcionario.html', var)