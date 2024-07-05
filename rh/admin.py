from django.contrib import admin
from .models import Funcionario, Cargos, Candidato, Recrutamento


admin.site.register(Funcionario)
admin.site.register(Cargos)
admin.site.register(Candidato)
admin.site.register(Recrutamento)

