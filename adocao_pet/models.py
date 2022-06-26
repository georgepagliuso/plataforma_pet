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
    idade = models.IntegerField(null=True, help_text="Anos")
    vacinas = models.ManyToManyField('Vacina', blank=True)
    peso = models.IntegerField(null=True, help_text="KG")
    microchip = models.IntegerField(null=True)
    localizacao = models.CharField(max_length=100, help_text="Formato: Cidade-Estado. Ex: Araraquara-SP")
    contato_email = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    alt_texto = models.CharField(max_length=100, help_text="Texto alternativo - Acessibilidade. Descreve de forma objetiva a aparência do pet.")

class Vacina(models.Model):
    nome=models.CharField(max_length=50)

    def __str__(self):
        return self.nome