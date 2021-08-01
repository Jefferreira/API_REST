from django.db import models


class Pokemon(models.Model):
    numero = models.IntegerField(primary_key=True, null=False, blank=False)
    nome = models.CharField(max_length=127)
    tipos = models.CharField(max_length=127)
    imagem_origem = models.URLField(max_length=127)

    def __str__(self):
        return self.nome

