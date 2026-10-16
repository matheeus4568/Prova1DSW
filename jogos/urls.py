from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('equipes/<id>', views.equipe, name='equipe'),
    path('modalidades/<id>', views.modalidade, name='modalidade'),
]