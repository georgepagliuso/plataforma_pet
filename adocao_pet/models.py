from re import M
from django.db import models

class Pet(models.Model):
    ESCOLHA_SEXO = [('M', 'Macho'), ('F', 'Fêmea')]
    nome = models.CharField(max_length=100)
    tutor = models.CharField(max_length=100)
    especie = models.CharField(max_length=30)
    raca = models.CharField(max_length=30, blank=True)
    descricao = models.TextField()
    sexo = models.CharField(max_length=1, choices=ESCOLHA_SEXO, blank=True)
    data_submissao = models.DateTimeField()
    idade = models.IntegerField(null=True)
    vacinas = models.ManyToManyField('Vacina', blank=True)
    peso = models.IntegerField(null=True)
    microchip = models.IntegerField(null=True)
    localizacao = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

class Vacina(models.Model):
    nome=models.CharField(max_length=50)

    def __str__(self):
        return self.nome