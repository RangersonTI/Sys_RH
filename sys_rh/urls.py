"""
URL configuration for sys_rh project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from rh import views as view_rh

urlpatterns = [
    # PATH DE LISTAGEM
    path('admin/', admin.site.urls),
    path('',view_rh.login, name='login'),
    path('login/',view_rh.login, name='login'),
    path('home/',view_rh.home, name='home'),
    path('funcionarios/', view_rh.funcionario, name='funcionario'),
    path('cargos/', view_rh.cargo, name='cargo'),
    path('recrutamento/', view_rh.recrutamento, name='recrutamento'),
    path('candidatos/', view_rh.candidatos,name='candidatos'),
    
    # PATH DE CADASTROS
    path('cad_cargo/', view_rh.cadcargo, name='cadcargo'),
    path('cad_candidato/',view_rh.cadcandidato,name='cadcandidato'),
    path('cad_funcionario/', view_rh.cadfuncionario, name='cadfuncionario'),
    path('cad_recrutamento/',view_rh.cadrecrutamento,name='cadrecrutamento'),

    # PATH DE EDIÇÃO
    path('edit_cargo/<int:id_cargo>', view_rh.editcargo, name='editcargo'),
    path('edit_candidato/<int:id_candidato>',view_rh.editcandidato,name='editcandidato'),
    path('edit_funcionario/<int:id_funcionario>', view_rh.editfuncionario, name='editfuncionario'),
    path('edit_recrutamento/<int:id_recrutamento>',view_rh.editrecrutamento,name='editrecrutamento')
]