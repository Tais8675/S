from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Lista, Produto
from django import forms

# Create your views here.

def index(request):
    return render(request, "lista/index.html", {
        "lista": Lista.objects.all()
    })

def lista(request, lista_id):
    lista = lista.objects.get(id=lista_id)
    produto = lista.produto.all()
    sem_lista = Produto.objects.exclude(id=lista_id).all()
    return render(request, "lista/lista.html", {
        "lista": lista,
        "produto": produto,
        "sem_lista": sem_lista
    })
