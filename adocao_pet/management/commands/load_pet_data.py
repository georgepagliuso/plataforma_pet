from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from adocao_pet.models import Pet, Vacina
import pytz
from pytz import UTC


DATETIME_FORMAT = '%d/%m/%Y %H:%M'

VACCINES_NAMES = [
    'Cinomose',
    'Parvovirose',
    'Adenovirose',
    'Leptospirose Canina',
    'Parainfluenza Canina'
]

ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the pet data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from pet_data.csv into our Pet mode"

    def handle(self, *args, **options):
        if Vacina.objects.exists() or Pet.objects.exists():
            print('Pet data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
        print("Creating vaccine data")
        for vaccine_name in VACCINES_NAMES:
            vac = Vacina(nome=vaccine_name)
            vac.save()
        print("Loading pet data for pets available for adoption")
        for row in DictReader(open('./pet_data.csv')):
            pet = Pet()
            pet.nome = row['Pet']
            pet.tutor = row['Tutor']
            pet.especie = row['Especie']
            pet.raca = row['Raca']
            pet.descricao = row['Descricao']
            pet.sexo = row['Sexo']
            raw_submission_date = row['Data_Submissao']
            pet.idade = row['Idade']
            pet.peso = row['Peso']
            pet.microchip = row['Microchip']
            pet.localizacao = row['Localizacao']
            data_submissao = UTC.localize(
                datetime.strptime(raw_submission_date, DATETIME_FORMAT))
            pet.data_submissao = data_submissao
            pet.save()
            raw_vaccination_names = row['Vacinas']
            vaccination_names = [name for name in raw_vaccination_names.split('| ') if name]
            for vac_name in vaccination_names:
                vac = Vacina.objects.get(nome=vac_name)
                pet.vacinas.add(vac)
            pet.save()
