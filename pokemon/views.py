from django.shortcuts import render
from django.views.generic import ListView, DetailView
from rest_framework import viewsets

from . import models, serializer


class Index(ListView):
    model = models.Pokemon
    template_name = 'pokemon/index.html'
    context_object_name = 'pokemons'
    ordering = ['numero']
    paginate_by = 50


class Detalhe(DetailView):
    model = models.Pokemon
    template_name = 'pokemon/detalhe.html'
    context_object_name = 'pokemon'


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = models.Pokemon.objects.all()
    serializer_class = serializer.PokemonSerializer

