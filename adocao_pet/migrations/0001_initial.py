# Generated by Django 3.2.9 on 2022-06-22 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('tutor', models.CharField(max_length=100)),
                ('especie', models.CharField(max_length=30)),
                ('raca', models.CharField(blank=True, max_length=30)),
                ('descricao', models.TextField()),
                ('sexo', models.CharField(blank=True, choices=[('M', 'Macho'), ('F', 'Fêmea')], max_length=1)),
                ('data_submissao', models.DateTimeField()),
                ('idade', models.IntegerField(null=True)),
                ('peso', models.IntegerField(null=True)),
                ('microchip', models.IntegerField(null=True)),
                ('localizacao', models.CharField(max_length=100)),
                ('vacinas', models.ManyToManyField(blank=True, to='adocao_pet.Vacina')),
            ],
        ),
    ]