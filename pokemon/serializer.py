from rest_framework import serializers

from . import models


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pokemon
        fields = ['numero', 'nome', 'tipos', 'imagem_origem']

