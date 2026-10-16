from django.db import models
from django.utils import timezone

# Create your models here.

class Modalidade(models.Model):
    TIPOS = {
        "Coletiva": "Coletiva",
        "Individual": "Individual"
             }

    nome = models.CharField(max_length=100, unique=True)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    max_atletas = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.nome}'

    class Meta:
        verbose_name = 'Modalidade'
        verbose_name_plural = 'Modalidades'


class Equipe(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    curso = models.CharField(max_length=100)
    cor = models.CharField(max_length=7)
    criada_em = models.DateTimeField(auto_now_add=timezone.now())

    def __str__(self):
        return f'{self.nome}'

    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'

    @property
    def qnt_atletas(self):
        return self.atletas.count()



class Tecnico(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=100, unique=True)
    tecnico = models.OneToOneField(Equipe, on_delete=models.CASCADE,null=True, blank=True, related_name='tecnico')

    def __str__(self):
        return f'{self.nome}'

    class Meta:
        verbose_name = 'Técnico'
        verbose_name_plural = 'Técnicos'


class Atleta(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=100, unique=True)
    data_nascimento = models.DateField()
    modalidades = models.ManyToManyField(Modalidade, blank=True, related_name='atletas')
    equipe = models.ForeignKey(Equipe, on_delete=models.PROTECT, null=True, blank=True, related_name='atletas')

    def __str__(self):
        return f'{self.nome}'

    class Meta:
        verbose_name = 'Atleta'
        verbose_name_plural = 'Atletas'