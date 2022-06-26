# Generated by Django 3.2.9 on 2022-06-26 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adocao_pet', '0003_auto_20220626_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='alt_texto',
            field=models.CharField(default=1, help_text='Texto alternativo - Acessibilidade. Descreve de forma objetiva a aparência do pet.', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pet',
            name='idade',
            field=models.IntegerField(help_text='Anos', null=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='peso',
            field=models.IntegerField(help_text='KG', null=True),
        ),
    ]
