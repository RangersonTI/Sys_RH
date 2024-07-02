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
    path('admin/', admin.site.urls),
    path('',view_rh.login, name='login'),
    path('login/',view_rh.login, name='login'),
    path('home/',view_rh.home, name='home'),
    path('funcionario/', view_rh.funcionario, name='funcionario'),
    path('cargo/', view_rh.cargo, name='cargo'),
    path('recrutamento/', view_rh.recrutamento, name='recrutamento'),
    path('cad_funcionario/', view_rh.cadfuncionario, name='cadfuncionario'),
    path('cad_cargo/', view_rh.cadcargo, name='cadcargo'),
]
