from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Modalidade)
class ModalidadeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo', 'max_atletas']
    ordering = ['nome']

@admin.register(Tecnico)
class TecnicoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'telefone']
    ordering = ['nome']

class TecnicoInline(admin.TabularInline):
    model = Tecnico
    extra = 1

@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'curso', 'qnt_atletas']
    ordering = ['nome']
    inlines = [TecnicoInline]


@admin.register(Atleta)
class AtletaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'matricula', 'equipe']
    list_filter = ['equipe', 'modalidades', ]
    search_fields = ['nome']
    ordering = ['nome']