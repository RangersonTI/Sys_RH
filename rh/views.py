from django.shortcuts import render

# Create your views here.

def home(request):

    var = {
        'titulo_pag': 'Home'
    }    
    return render(request, 'pages/home.html', var)

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