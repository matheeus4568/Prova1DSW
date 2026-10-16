from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Modalidade)
class ModalidadeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo', 'max_atletas']
    ordering = ['nome']

@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'curso', 'cor', 'criada_em']
    ordering = ['nome']

@admin.register(Tecnico)
class TecnicoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'telefone']
    ordering = ['nome']

@admin.register(Atleta)
class AtletaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'matricula', 'data_nascimento']
    ordering = ['nome']