from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def index(request):
    equipes = Equipe.objects.all()
    modalidades = Modalidade.objects.all()

    contexto = {
        'equipes': equipes,
        'modalidades': modalidades,
    }

    return render(request, 'jogos/index.html', contexto)

def equipe(request, id):
    equipe = get_object_or_404(Equipe, pk=id)
    atletas = Atleta.objects.filter(equipe=equipe)

    contexto = {
        'equipe': equipe,
        'atletas': atletas,
    }
    
    return render(request, 'jogos/equipe.html', contexto)

def modalidade(request, id):
    modalidade = get_object_or_404(Modalidade, pk=id)
    atletas = Atleta.objects.filter(modalidades=modalidade)

    contexto = {
        'modalidade': modalidade,
        'atletas': atletas,
    }
    
    return render(request, 'jogos/modalidade.html', contexto)